from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm
from .models import (
    AboutSection,
    BlogPost,
    ClientLogo,
    CounterStat,
    Download,
    FeatureBlock,
    HeroSlide,
    LegalPage,
    Project,
    SectionHeading,
    Service,
    SuccessStory,
    TeamMember,
    Testimonial,
)


def _heading(page, section_key):
    try:
        return SectionHeading.objects.get(page=page, section_key=section_key)
    except SectionHeading.DoesNotExist:
        return None


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your message has been sent.')
            return redirect('home')
    else:
        form = ContactForm()

    featured_posts = BlogPost.objects.filter(is_published=True, is_featured=True)[:1]
    sidebar_posts = BlogPost.objects.filter(is_published=True, is_featured=False)[:2]

    context = {
        'hero_slides': HeroSlide.objects.filter(is_active=True),
        'about': AboutSection.load(),
        'features': FeatureBlock.objects.all(),
        'counter_heading': _heading('home', 'counters'),
        'counters': CounterStat.objects.filter(is_active=True),
        'success_story': SuccessStory.load(),
        'services_heading': _heading('home', 'services'),
        'services': Service.objects.filter(is_active=True),
        'team_heading': _heading('home', 'team'),
        'team_members': TeamMember.objects.filter(is_active=True)[:4],
        'projects_heading': _heading('home', 'projects'),
        'projects': Project.objects.filter(is_active=True)[:6],
        'testimonials_heading': _heading('home', 'testimonials'),
        'testimonials': Testimonial.objects.filter(is_active=True),
        'blog_heading': _heading('home', 'blog'),
        'featured_post': featured_posts.first(),
        'sidebar_posts': sidebar_posts,
        'clients': ClientLogo.objects.filter(is_active=True),
        'downloads': Download.objects.filter(is_active=True),
        'contact_form': form,
        'page_title': 'Home',
    }
    return render(request, 'index.html', context)


def coming_soon(request):
    return render(request, 'coming-soon.html', {'page_title': 'Coming Soon'})


def team(request):
    context = {
        'page_heading': _heading('team', 'main'),
        'team_heading': _heading('team', 'grid'),
        'team_members': TeamMember.objects.filter(is_active=True),
        'clients': ClientLogo.objects.filter(is_active=True),
        'downloads': Download.objects.filter(is_active=True),
        'page_title': 'Team',
    }
    return render(request, 'team.html', context)


def team_detail(request, slug):
    member = get_object_or_404(TeamMember, slug=slug, is_active=True)
    return render(request, 'team-detail.html', {
        'member': member,
        'page_title': member.name,
    })


def projects(request):
    context = {
        'page_heading': _heading('projects', 'main'),
        'projects': Project.objects.filter(is_active=True),
        'clients': ClientLogo.objects.filter(is_active=True),
        'downloads': Download.objects.filter(is_active=True),
        'page_title': 'Projects',
    }
    return render(request, 'projects.html', context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug, is_active=True)
    return render(request, 'news-detail.html', {
        'project': project,
        'page_title': project.title,
    })


def blog(request):
    context = {
        'page_heading': _heading('blog', 'main'),
        'posts': BlogPost.objects.filter(is_published=True),
        'clients': ClientLogo.objects.filter(is_active=True),
        'downloads': Download.objects.filter(is_active=True),
        'page_title': 'Blog',
    }
    return render(request, 'blog.html', context)


def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    return render(request, 'news-detail.html', {
        'post': post,
        'page_title': post.title,
    })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your message has been sent.')
            return redirect('contact')
    else:
        form = ContactForm()

    context = {
        'page_heading': _heading('contact', 'main'),
        'contact_form': form,
        'clients': ClientLogo.objects.filter(is_active=True),
        'downloads': Download.objects.filter(is_active=True),
        'page_title': 'Contact',
    }
    return render(request, 'contact.html', context)


def terms(request):
    page = get_object_or_404(LegalPage, slug='terms')
    return render(request, 'terms.html', {
        'legal_page': page,
        'clients': ClientLogo.objects.filter(is_active=True),
        'downloads': Download.objects.filter(is_active=True),
        'page_title': page.title,
    })


def privacy(request):
    page = get_object_or_404(LegalPage, slug='privacy')
    return render(request, 'privacy.html', {
        'legal_page': page,
        'clients': ClientLogo.objects.filter(is_active=True),
        'downloads': Download.objects.filter(is_active=True),
        'page_title': page.title,
    })
