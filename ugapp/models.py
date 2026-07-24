from django.db import models
from django.utils.text import slugify


class ImageMixin:
    """Prefer uploaded image; fall back to static asset path."""

    def get_image_url(self):
        if self.image:
            return self.image.url
        if getattr(self, 'static_image', None):
            return f'/static/{self.static_image.lstrip("/")}'
        return ''


class SiteSettings(models.Model):
    company_name = models.CharField(max_length=200, default='UGACloud')
    site_title = models.CharField(max_length=200, default='UGACloud | IT Solutions')
    hiring_banner = models.CharField(
        max_length=300,
        blank=True,
        default='Now Hiring: Are you a driven and motivated IT professional?',
    )
    signup_url = models.CharField(max_length=200, blank=True, default='#')
    address = models.CharField(max_length=300, default='Division St, Los Angeles, USA')
    business_hours = models.CharField(max_length=100, default='9:00am To 6pm')
    phone = models.CharField(max_length=50, default='(212) 232-4499')
    email = models.EmailField(blank=True, default='info@ugacloud.com')
    logo = models.ImageField(upload_to='site/', blank=True)
    static_logo = models.CharField(max_length=200, default='images/logo-4.png')
    mobile_logo = models.ImageField(upload_to='site/', blank=True)
    static_mobile_logo = models.CharField(max_length=200, default='images/logo-5.png')
    facebook_url = models.URLField(blank=True, default='https://facebook.com/')
    twitter_url = models.URLField(blank=True, default='https://twitter.com/')
    google_url = models.URLField(blank=True, default='https://google.com/')
    pinterest_url = models.URLField(blank=True, default='https://pinterest.com/')
    footer_about = models.TextField(
        blank=True,
        default='We help digital companies scale their business and get results.',
    )
    copyright_text = models.CharField(
        max_length=200,
        default='Copyright © 2026 UGACloud All Rights Reserved.',
    )

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.company_name

    def logo_url(self):
        if self.logo:
            return self.logo.url
        return f'/static/{self.static_logo.lstrip("/")}'

    def mobile_logo_url(self):
        if self.mobile_logo:
            return self.mobile_logo.url
        return f'/static/{self.static_mobile_logo.lstrip("/")}'

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class SectionHeading(models.Model):
    PAGE_CHOICES = [
        ('home', 'Home'),
        ('team', 'Team'),
        ('projects', 'Projects'),
        ('blog', 'Blog'),
        ('contact', 'Contact'),
    ]
    page = models.CharField(max_length=50, choices=PAGE_CHOICES)
    section_key = models.CharField(max_length=50)
    eyebrow = models.CharField(max_length=200, blank=True)
    title = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = ('page', 'section_key')
        ordering = ['page', 'section_key']

    def __str__(self):
        return f'{self.page} / {self.section_key}'


class HeroSlide(models.Model, ImageMixin):
    grow_text = models.CharField(max_length=200, blank=True)
    headline = models.CharField(max_length=300, blank=True)
    headline_html = models.TextField(
        blank=True,
        help_text='Optional HTML for styled headline. Overrides plain headline when set.',
    )
    description = models.TextField(blank=True)
    background_image = models.ImageField(upload_to='hero/', blank=True)
    static_background = models.CharField(max_length=200, default='images/main-slider/1.jpg')
    slide_image = models.ImageField(upload_to='hero/', blank=True)
    static_slide_image = models.CharField(max_length=200, default='images/main-slider/image-3.png')
    cta_text = models.CharField(max_length=100, default='Get in Touch')
    cta_url = models.CharField(max_length=200, default='/contact/')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.headline

    def background_url(self):
        if self.background_image:
            return self.background_image.url
        return f'/static/{self.static_background.lstrip("/")}'

    def slide_image_url(self):
        if self.slide_image:
            return self.slide_image.url
        return f'/static/{self.static_slide_image.lstrip("/")}'


class AboutSection(models.Model):
    eyebrow = models.CharField(max_length=200, default='DELIVER LATEST SERVICES')
    title = models.CharField(max_length=300, default='About Our Company')
    body = models.TextField(default='Tell your company story here.')
    skill_name = models.CharField(max_length=100, blank=True)
    skill_percent = models.PositiveIntegerField(default=70)
    bullet_points = models.TextField(
        blank=True,
        help_text='One bullet point per line.',
    )
    signature_image = models.ImageField(upload_to='about/', blank=True)
    static_signature = models.CharField(max_length=200, default='images/icons/signature-1.png')
    main_image = models.ImageField(upload_to='about/', blank=True)
    static_main_image = models.CharField(max_length=200, default='images/resource/about-5.jpg')
    since_year = models.PositiveIntegerField(default=2012)

    class Meta:
        verbose_name = 'About Section'
        verbose_name_plural = 'About Section'

    def __str__(self):
        return self.title

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    def bullets(self):
        return [line.strip() for line in self.bullet_points.splitlines() if line.strip()]

    def signature_url(self):
        if self.signature_image:
            return self.signature_image.url
        return f'/static/{self.static_signature.lstrip("/")}'

    def main_image_url(self):
        if self.main_image:
            return self.main_image.url
        return f'/static/{self.static_main_image.lstrip("/")}'


class FeatureBlock(models.Model):
    icon_class = models.CharField(max_length=100, default='flaticon-internet')
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class CounterStat(models.Model):
    icon_class = models.CharField(max_length=100, default='flaticon-dashboard')
    value = models.PositiveIntegerField(default=0)
    suffix = models.CharField(max_length=10, default='+')
    label = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.value}{self.suffix} {self.label}'


class SuccessStory(models.Model):
    icon_class = models.CharField(max_length=100, default='flaticon-diagram')
    value = models.PositiveIntegerField(default=35)
    suffix = models.CharField(max_length=10, default='+')
    text = models.CharField(max_length=200, default='Learn more about our Success Stories')

    class Meta:
        verbose_name = 'Success Story Highlight'
        verbose_name_plural = 'Success Story Highlight'

    def __str__(self):
        return self.text

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Service(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100, default='flaticon-photo-editing')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='services/', blank=True)
    static_image = models.CharField(max_length=200, default='images/resource/service-4.jpg')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def image_url(self):
        if self.image:
            return self.image.url
        return f'/static/{self.static_image.lstrip("/")}'


class TeamMember(models.Model, ImageMixin):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    role = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='team/', blank=True)
    static_image = models.CharField(max_length=200, default='images/resource/team-5.jpg')
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    dribbble_url = models.URLField(blank=True)
    google_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Project(models.Model, ImageMixin):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    static_image = models.CharField(max_length=200, default='images/gallery/7.jpg')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Testimonial(models.Model, ImageMixin):
    quote = models.TextField()
    author_name = models.CharField(max_length=200)
    author_role = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='testimonials/', blank=True)
    static_image = models.CharField(max_length=200, default='images/resource/author-4.jpg')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.author_name


class BlogPost(models.Model, ImageMixin):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True)
    author = models.CharField(max_length=200)
    published_date = models.DateField()
    excerpt = models.TextField()
    body = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True)
    static_image = models.CharField(max_length=200, default='images/resource/news-7.jpg')
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(
        default=False,
        help_text='Featured posts appear with large image on the homepage.',
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-published_date', 'order']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def formatted_date(self):
        return self.published_date.strftime('%d / %m / %Y')


class ClientLogo(models.Model, ImageMixin):
    name = models.CharField(max_length=200)
    url = models.URLField(blank=True, default='#')
    image = models.ImageField(upload_to='clients/', blank=True)
    static_image = models.CharField(max_length=200, default='images/clients/1.png')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class Download(models.Model):
    title = models.CharField(max_length=100, default='Software')
    subtitle = models.CharField(max_length=200)
    file = models.FileField(upload_to='downloads/', blank=True)
    file_url = models.URLField(blank=True, help_text='External download link if no file uploaded.')
    file_size_label = models.CharField(max_length=50, default='Download')
    icon = models.ImageField(upload_to='downloads/', blank=True)
    static_icon = models.CharField(max_length=200, default='images/icons/pdf.png')
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.subtitle

    def icon_url(self):
        if self.icon:
            return self.icon.url
        return f'/static/{self.static_icon.lstrip("/")}'

    def download_href(self):
        if self.file:
            return self.file.url
        return self.file_url or '#'


class LegalPage(models.Model):
    SLUG_CHOICES = [
        ('terms', 'Terms of Use'),
        ('privacy', 'Privacy Policy'),
    ]
    slug = models.SlugField(choices=SLUG_CHOICES, unique=True)
    title = models.CharField(max_length=200)
    content = models.TextField()

    class Meta:
        verbose_name = 'Legal Page'
        verbose_name_plural = 'Legal Pages'

    def __str__(self):
        return self.title


class ContactSubmission(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.subject}'
