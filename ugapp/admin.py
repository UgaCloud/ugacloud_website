from django.contrib import admin

from .models import (
    AboutSection,
    BlogPost,
    ClientLogo,
    ContactSubmission,
    CounterStat,
    Download,
    FeatureBlock,
    HeroSlide,
    LegalPage,
    Project,
    SectionHeading,
    Service,
    SiteSettings,
    SuccessStory,
    TeamMember,
    Testimonial,
)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Branding', {
            'fields': ('company_name', 'site_title', 'logo', 'static_logo', 'mobile_logo', 'static_mobile_logo'),
        }),
        ('Header Top Bar', {
            'fields': ('hiring_banner', 'signup_url'),
        }),
        ('Contact Info', {
            'fields': ('address', 'business_hours', 'phone', 'email'),
        }),
        ('Social Links', {
            'fields': ('facebook_url', 'twitter_url', 'google_url', 'pinterest_url'),
        }),
        ('Footer', {
            'fields': ('footer_about', 'copyright_text'),
        }),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(SectionHeading)
class SectionHeadingAdmin(admin.ModelAdmin):
    list_display = ('page', 'section_key', 'title')
    list_filter = ('page',)
    search_fields = ('section_key', 'title')


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('headline', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_filter = ('is_active',)


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not AboutSection.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(FeatureBlock)
class FeatureBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)


@admin.register(CounterStat)
class CounterStatAdmin(admin.ModelAdmin):
    list_display = ('label', 'value', 'suffix', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(SuccessStory)
class SuccessStoryAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SuccessStory.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'category')


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'role')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'category')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'author_role', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'is_published', 'is_featured')
    list_editable = ('is_published', 'is_featured')
    list_filter = ('is_published', 'is_featured', 'published_date')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'author')
    date_hierarchy = 'published_date'


@admin.register(ClientLogo)
class ClientLogoAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
    list_display = ('subtitle', 'title', 'file_size_label', 'order', 'is_active')
    list_editable = ('order', 'is_active')


@admin.register(LegalPage)
class LegalPageAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title')


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'is_read')
    list_filter = ('is_read', 'created_at')
    list_editable = ('is_read',)
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')

    def has_add_permission(self, request):
        return False


admin.site.site_header = 'UGACloud Site Manager'
admin.site.site_title = 'UGACloud Admin'
admin.site.index_title = 'Manage Website Content'


admin.site.site_header = 'UGACloud Site Manager'
admin.site.site_title = 'UGACloud Admin'
admin.site.index_title = 'Manage Website Content'
