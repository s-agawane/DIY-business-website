from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.forms import EmailField
from django.http import HttpResponse
from django.utils.html import strip_tags
from django.views.generic import TemplateView

from core.models import (About, Carousel, Contact, ContactEmail, Package,
                         Portfolio, Product, Service, Social, Testimonial,
                         WebsiteConfig)


class SiteView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(SiteView, self).get_context_data(**kwargs)
        context = {
            'contact': Contact.objects.filter(is_active=True).prefetch_related('emails', 'numbers').first(),
            'websiteconfig': WebsiteConfig.objects.filter(is_active=True).first(),
            'social': Social.objects.filter(is_active=True).first(),
            'about': About.objects.filter(is_active=True).first(),
            'portfolios': Portfolio.objects.filter(is_published=True).prefetch_related('images'),
            'packages': Package.objects.filter(is_published=True).prefetch_related('features'),
            'products': Product.objects.filter(is_published=True),
            'carousels': Carousel.objects.filter(is_published=True),
            'services': Service.objects.filter(is_published=True),
            'testimonials': Testimonial.objects.filter(is_published=True),
        }
        return context


def contact(request, *args, **kwargs):
    """
    Send mail
    """
    message = "There was a problem with your submission, please try again."
    status = 403
    if request.method == "POST":
        try:
            name = strip_tags(
                request.POST.get('name').strip().replace("\r\n", " ")
            )
            from_mail = EmailField().clean(request.POST.get('email').strip())
            massage = request.POST.get('massage').strip()
            to_mail = ContactEmail.objects.filter(
                contact__is_active=True,
                is_contact_email=True
            ).only('email').first()
            if all([name, from_mail, massage]):
                message = "Oops! Something went wrong and we couldn't send your message.",
                status = 500
                if send_mail(
                    'New contact from ' + name,
                    'First Name: {}\nEmail: {}\n\nMessage:\n{}\n'.format(
                        name,
                        from_mail,
                        massage
                    ),
                    name + ' <' + from_mail + '>',
                    [to_mail],
                    fail_silently=False,
                ):
                    message = "Thank You! Your message has been sent.",
                    status = 200
        except ValidationError as e:
            message = e
            status = 400
    return HttpResponse(
        message,
        status=status
    )
