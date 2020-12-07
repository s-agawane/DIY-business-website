from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from core.models import (About, Carousel, Contact, ContactEmail, ContactNumber,
                         Package, PackageFeature, Portfolio, PortfolioImage,
                         Product, Service, Social, Testimonial, WebsiteConfig)


class PortfolioImageAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = PortfolioImage


@admin.register(Portfolio)
class PortfolioAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = (PortfolioImageAdmin, )


class ContactEmailAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = ContactEmail


class ContactNumberAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = ContactNumber


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = (ContactEmailAdmin, ContactNumberAdmin)


class PackageFeatureAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = PackageFeature


@admin.register(Package)
class PackageAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = (PackageFeatureAdmin, )


@admin.register(Carousel)
class CarouselAdmin(SortableAdminMixin, ModelAdmin):
    pass


@admin.register(Service)
class ServiceAdmin(SortableAdminMixin, ModelAdmin):
    pass


@admin.register(Testimonial)
class TestimonialAdmin(SortableAdminMixin, ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(SortableAdminMixin, ModelAdmin):
    pass


admin.site.register(WebsiteConfig)
admin.site.register(About)
admin.site.register(Social)
