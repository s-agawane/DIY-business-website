from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from django.utils.html import format_html

from core.models import (About, Carousel, Contact, ContactEmail, ContactNumber,
                         Package, PackageFeature, Portfolio, PortfolioImage,
                         Product, Service, Social, Testimonial, WebsiteConfig)


class PortfolioImageAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = PortfolioImage


@admin.register(Portfolio)
class PortfolioAdmin(SortableAdminMixin, admin.ModelAdmin):

    list_display = (
        '__str__',
        'is_published'
    )
    inlines = (PortfolioImageAdmin, )


class ContactEmailAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = ContactEmail


class ContactNumberAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = ContactNumber


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    def get_queryset(self, obj):
        qs = super(ContactAdmin, self).get_queryset(obj)
        return qs.prefetch_related('emails', 'numbers')

    def get_emails(self, obj):
        return format_html(
            "<br>".join(
                [
                    email.__str__() for email in obj.emails.all()
                ]
            )
        )

    def get_numbers(self, obj):
        return format_html(
            "<br>".join(
                [
                    number.__str__() for number in obj.numbers.all()
                ]
            )
        )

    def address_html(self, obj) -> str:
        return format_html(
            '{}'.format(
                obj.address
            )
        )

    address_html.short_description = 'Address'
    get_emails.short_description = 'Emails'
    get_numbers.short_description = 'Contact Nos.'

    list_display = (
        'address_html',
        'get_emails',
        'get_numbers',
        'is_active'
    )
    inlines = (ContactEmailAdmin, ContactNumberAdmin)


class PackageFeatureAdmin(SortableInlineAdminMixin, admin.StackedInline):
    model = PackageFeature


@admin.register(Package)
class PackageAdmin(SortableAdminMixin, admin.ModelAdmin):

    def image_tag(self, obj):
        try:
            return format_html(
                '<img src="{}" style="max-width: 100px;"/>'.format(
                    obj.image.url
                )
            )
        except ValueError:
            return None

    image_tag.short_description = 'Package Image'

    list_display = (
        'title',
        'image_tag',
        'original_price',
        'discount_price',
        'is_published',
    )
    inlines = (PackageFeatureAdmin, )


@admin.register(Carousel)
class CarouselAdmin(SortableAdminMixin, ModelAdmin):

    list_display = (
        '__str__',
        'is_published'
    )


@admin.register(Service)
class ServiceAdmin(SortableAdminMixin, ModelAdmin):

    def image_tag(self, obj):
        try:
            return format_html(
                '<img src="{}" style="max-width: 75px;"/>'.format(
                    obj.image.url
                )
            )
        except ValueError:
            return None

    image_tag.short_description = 'Service Image'

    list_display = (
        '__str__',
        'image_tag',
        'is_published'
    )


@admin.register(Testimonial)
class TestimonialAdmin(SortableAdminMixin, ModelAdmin):

    def image_tag(self, obj):
        try:
            return format_html(
                '<img src="{}" style="max-width: 75px;"/>'.format(
                    obj.user_profile_pic.url
                )
            )
        except ValueError:
            return None

    image_tag.short_description = 'Profile Image'

    list_display = (
        'username',
        'image_tag',
        'is_published'
    )


@admin.register(Product)
class ProductAdmin(SortableAdminMixin, ModelAdmin):

    def image_tag(self, obj):
        return format_html(
            '<img src="{}" style="max-width: 100px;"/>'.format(
                obj.image.url
            )
        )

    image_tag.short_description = 'Product Image'

    list_display = (
        'title',
        'image_tag',
        'original_price',
        'discount_price',
        'is_published',
    )


@admin.register(About)
class AboutAdmin(ModelAdmin):

    list_display = (
        '__str__',
        'is_active'
    )


@admin.register(WebsiteConfig)
class WebsiteConfigAdmin(ModelAdmin):

    def image_tag(self, obj):
        try:
            return format_html(
                '<img src="{}" style="max-width: 100px;"/>'.format(
                    obj.logo_dark.url
                )
            )
        except ValueError:
            return None

    image_tag.short_description = 'Logo (DARK)'

    list_display = (
        '__str__',
        'image_tag',
        'is_active'
    )


@admin.register(Social)
class SocialAdmin(ModelAdmin):

    list_display_1 = ['__str__']
    list_display_2 = [
        field.name for field in Social._meta.fields if field.name != "id"
    ]
    list_display = list_display_1 + list_display_2
