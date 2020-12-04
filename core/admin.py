from django.contrib import admin

from core.models import (About, Carousel, Contact, ContactEmail, ContactNumber,
                         Package, PackageFeature, Portfolio, PortfolioImage,
                         Service, Social, Testimonial, WebsiteConfig)


class PortfolioImageAdmin(admin.TabularInline):
    model = PortfolioImage


class PortfolioAdmin(admin.ModelAdmin):
    inlines = [PortfolioImageAdmin, ]


class ContactEmailAdmin(admin.TabularInline):
    model = ContactEmail


class ContactNumberAdmin(admin.TabularInline):
    model = ContactNumber


class ContactAdmin(admin.ModelAdmin):
    inlines = [ContactEmailAdmin, ContactNumberAdmin]


class ProductFeatureAdmin(admin.TabularInline):
    model = PackageFeature


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductFeatureAdmin, ]


admin.site.register(WebsiteConfig)
admin.site.register(Carousel)
admin.site.register(Service)
admin.site.register(About)
admin.site.register(Social)
admin.site.register(Testimonial)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Package, ProductAdmin)
