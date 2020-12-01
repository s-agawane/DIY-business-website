from core.models import About, Contact, Portfolio, Product, Service, Social, WebsiteConfig, Carousel


def config_data(*args, **kwargs):

    return {
        'websiteconfig': WebsiteConfig.objects.filter(is_active=True).first(),
        'carousels': Carousel.objects.filter(is_published=True),
        'services': Service.objects.filter(is_published=True),
        'portfolios': Portfolio.objects.filter(is_published=True),
        'about': About.objects.filter(is_active=True).first(),
        'social': Social.objects.filter(is_active=True).first(),
        'contact': Contact.objects.filter(is_active=True).first(),
        'products': Product.objects.filter(is_published=True)
    }
