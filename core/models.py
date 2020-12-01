from colorfield.fields import ColorField
from django.db import models
from djrichtextfield.models import RichTextField


class WebsiteConfig(models.Model):
    """
    Website Config
    """
    title = models.CharField(
        max_length=256,
        help_text="Website Title"
    )
    logo = models.FileField(
        help_text="Website Logo",
        upload_to='assets/logo/'
    )
    services_description = RichTextField(
        blank=True,
        null=True,
        help_text="Services Section Description"
    )
    gallery_description = RichTextField(
        blank=True,
        null=True,
        help_text="Gallery Section Description"
    )
    copyright_info = RichTextField(
        blank=True,
        null=True,
        help_text="Copyright Information"
    )
    is_active = models.BooleanField(
        default=True
    )

    def save(self, *args, **kwargs):
        if self.is_active:
            WebsiteConfig.objects.filter(
                is_active=True
            ).update(
                is_active=False
            )
        super(WebsiteConfig, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return '{} {}'.format(
            self.title,
            self.copyright_info
        )

    class Meta:
        db_table = "tbl_website_config"


class Carousel(models.Model):
    """
    Carousel Config
    """
    title = models.CharField(
        max_length=256,
        help_text="Carousel Item Title"
    )
    image = models.FileField(
        help_text="Carousel Item Image",
        upload_to='assets/images/carousels/'
    )
    description = RichTextField(
        blank=True,
        null=True,
        help_text="Carousel Item Description"
    )
    background_color = ColorField(
        help_text="Carousel Item Background Color",
        default="#0067f4"
    )
    is_published = models.BooleanField(
        db_index=True,
        default=False
    )

    def __str__(self) -> str:
        return '{} - {}'.format(
            self.title,
            self.description
        )

    class Meta:
        db_table = "tbl_carousels"


class Service(models.Model):
    """
    Services Config
    """
    title = models.CharField(
        max_length=256,
        help_text="Service Title"
    )
    image = models.FileField(
        blank=True,
        null=True,
        help_text="Service Image",
        upload_to='assets/images/services/'
    )
    description = RichTextField(
        blank=True,
        null=True,
        help_text="Service Description"
    )
    icon_class = models.CharField(
        blank=True,
        null=True,
        max_length=100,
        help_text="Choose from https://lineicons.com/icons/ (lni lni-whatsapp) or https://fontawesome.com/icons?d=gallery&m=free (fas fa-whatsapp)"
    )
    is_published = models.BooleanField(
        db_index=True,
        default=False
    )

    def __str__(self) -> str:
        return '{} - {}'.format(
            self.title,
            self.description
        )

    class Meta:
        db_table = "tbl_services"


class Portfolio(models.Model):
    """
    Portfolio Config
    """
    title = models.CharField(
        max_length=256,
        help_text="Portfolio Title"
    )
    is_published = models.BooleanField(
        db_index=True,
        default=False
    )

    def __str__(self) -> str:
        return '{}'.format(
            self.title
        )

    class Meta:
        db_table = "tbl_portfolios"


class PortfolioImage(models.Model):
    """
    Portfolio Image
    """
    portfolio = models.ForeignKey(
        Portfolio,
        on_delete=models.CASCADE,
        related_name="images",
        help_text="Choose Portfolio Category"
    )
    image = models.FileField(
        help_text="Portfolio Category Image",
        upload_to='assets/images/portfolio/'
    )

    def __str__(self) -> str:
        return '{} - ({})'.format(
            self.image,
            self.portfolio.__str__()
        )

    class Meta:
        db_table = "tbl_portfolio_images"


class Contact(models.Model):
    """
    Contact Information
    """
    address = RichTextField(
        help_text="Elizabeth St, Melbourne 1202 Australia."
    )
    maps_src = models.URLField(
        blank=True,
        null=True,
        max_length=256,
        help_text="Url for map embed. e.g. https://maps.google.com/maps?q=Mission%20District%2C%20San%20Francisco%2C%20CA%2C%20USA&t=&z=13&ie=UTF8&iwloc=&output=embed",
    )
    description = RichTextField(
        blank=True,
        null=True,
        help_text="Contact Us Section Description"
    )
    whatsapp = models.CharField(
        blank=True,
        null=True,
        max_length=30,
        help_text="Whatsapp mobile no. +9188xxxxxx"
    )
    whatsapp_text = models.TextField(
        blank=True,
        null=True,
        help_text="Whatsapp default message template."
    )
    is_active = models.BooleanField(
        default=True
    )

    def save(self, *args, **kwargs):
        if self.is_active:
            Contact.objects.filter(
                is_active=True
            ).update(
                is_active=False
            )
        super(Contact, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return '{}'.format(
            self.address
        )

    class Meta:
        db_table = "tbl_contacts"


class ContactEmail(models.Model):
    """
    Contact Email
    """
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name="emails",
        help_text="Choose Contact"
    )
    email = models.EmailField(
        help_text="support@uideck.com"
    )

    def __str__(self) -> str:
        return '{} - ({})'.format(
            self.email,
            self.contact.__str__()
        )

    class Meta:
        db_table = "tbl_contact_emails"


class ContactNumber(models.Model):
    """
    Contact Number
    """
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        related_name="numbers",
        help_text="Choose Contact"
    )
    number = models.CharField(
        max_length=20,
        help_text="+9188xxxxxx"
    )

    def __str__(self) -> str:
        return '{} - ({})'.format(
            self.number,
            self.contact.__str__()
        )

    class Meta:
        db_table = "tbl_contact_numbers"


class About(models.Model):
    """
    About Us Information
    """
    description = RichTextField(
        blank=True,
        null=True,
        help_text="About Us Section Description"
    )
    is_active = models.BooleanField(
        default=True
    )

    def save(self, *args, **kwargs):
        if self.is_active:
            About.objects.filter(
                is_active=True
            ).update(
                is_active=False
            )
        super(About, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return '{}'.format(
            self.description
        )

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About Us"
        db_table = "tbl_about"


class Social(models.Model):
    """
    Social Accounts Information
    """
    facebook = models.URLField(
        blank=True,
        null=True,
        help_text="https://facebook.com/uideckHQ"
    )
    twitter = models.URLField(
        blank=True,
        null=True,
        help_text="https://twitter.com/uideckHQ"
    )
    instagram = models.URLField(
        blank=True,
        null=True,
        help_text="https://instagram.com/uideckHQ"
    )
    linkedin = models.URLField(
        blank=True,
        null=True,
        help_text="https://www.linkedin.com/in/linkedinyourname."
    )
    is_active = models.BooleanField(
        default=True
    )

    def save(self, *args, **kwargs):
        if self.is_active:
            Social.objects.filter(
                is_active=True
            ).update(
                is_active=False
            )
        super(Social, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Social Account Information"
        verbose_name_plural = "Social Accounts"
        db_table = "tbl_social_accounts"


class Product(models.Model):
    """
    Product
    """
    title = models.CharField(
        max_length=256,
        help_text="Product Title"
    )
    price = models.CharField(
        max_length=50,
        help_text="Product Price"
    )
    price_text = models.CharField(
        max_length=50,
        help_text="After price text"
    )
    is_published = models.BooleanField(
        db_index=True,
        default=False
    )

    def __str__(self) -> str:
        return '{} - {}{}'.format(
            self.title,
            self.price,
            self.price_text
        )

    class Meta:
        db_table = "tbl_products"


class ProductFeature(models.Model):
    """
    Product Feature
    """
    product = models.ForeignKey(
        Product,
        related_name='features',
        on_delete=models.CASCADE,
        help_text="Choose Product"
    )
    title = models.CharField(
        max_length=256,
        help_text="Product Feature Title"
    )

    def __str__(self) -> str:
        return '{} - ({})'.format(
            self.title,
            self.product.__str__()
        )

    class Meta:
        db_table = "tbl_product_features"
