from django.views.generic import TemplateView

from core.models import (About, Carousel, Contact, Package, Portfolio, Product,
                         Service, Social, Testimonial, WebsiteConfig)


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
