from datetime import date

from django.core.management.base import BaseCommand

from ugapp.models import (
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
    SiteSettings,
    SuccessStory,
    TeamMember,
    Testimonial,
)


class Command(BaseCommand):
    help = 'Seed the database with default website content from the template.'

    def handle(self, *args, **options):
        self.stdout.write('Seeding site content...')

        SiteSettings.objects.update_or_create(
            pk=1,
            defaults={
                'company_name': 'UGACloud',
                'site_title': 'UGACloud | IT Solutions & Consulting',
                'hiring_banner': 'Now Hiring: Are you a driven and motivated IT Support Engineer?',
                'address': 'Division St, Los Angeles, USA',
                'business_hours': '9:00am To 6pm',
                'phone': '(212) 232-4499',
                'email': 'info@ugacloud.com',
                'footer_about': (
                    'We are a leading Information Technology company providing '
                    'high-quality hardware and network solutions with over 25 years of experience.'
                ),
                'copyright_text': 'Copyright © 2026 UGACloud All Rights Reserved.',
            },
        )

        AboutSection.objects.update_or_create(
            pk=1,
            defaults={
                'eyebrow': 'DELIVER LATEST SERVICES',
                'title': 'We Execute IT Related Case The Investigations & Work',
                'body': (
                    'On the other hand we denounce with righteous indignation and dislike men '
                    'who are so beguiled and demoralized by the charms of pleasure of the moment.'
                ),
                'skill_name': 'Business Development',
                'skill_percent': 70,
                'bullet_points': (
                    'Exploring version of lorem veritatis Proin\n'
                    'Auctor aliquet aenean veritatis quis\n'
                    'Consequat ipsum nec sagittis sem nibh.'
                ),
                'since_year': 2012,
            },
        )

        SuccessStory.objects.update_or_create(
            pk=1,
            defaults={'value': 35, 'text': 'Learn more about our Success Stories'},
        )

        if not HeroSlide.objects.exists():
            slides = [
                {
                    'grow_text': 'Grow <span> &amp; </span> Nuture <br> <span>the</span> Ideas <span>You</span> Have.',
                    'headline_html': 'Digital <span>Enterprice app</span><strong>Development</strong>',
                    'description': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry.',
                    'order': 0,
                },
                {
                    'grow_text': 'Grow <span> &amp; </span> Nuture <br> <span>the</span> Ideas <span>You</span> Have.',
                    'headline_html': 'Cloud <span>Infrastructure</span><strong>Solutions</strong>',
                    'description': 'Scalable cloud services tailored to your business needs.',
                    'order': 1,
                },
                {
                    'grow_text': 'Grow <span> &amp; </span> Nuture <br> <span>the</span> Ideas <span>You</span> Have.',
                    'headline_html': 'Enterprise <span>Software</span><strong>Development</strong>',
                    'description': 'Custom software solutions that drive business growth.',
                    'order': 2,
                },
            ]
            for slide in slides:
                HeroSlide.objects.create(**slide, cta_url='/contact/')

        if not FeatureBlock.objects.exists():
            FeatureBlock.objects.bulk_create([
                FeatureBlock(
                    icon_class='flaticon-internet',
                    title='Website Development',
                    description='Duis eleifend molestie leo at mollis sanctus intro.',
                    order=0,
                ),
                FeatureBlock(
                    icon_class='flaticon-data-science',
                    title='Internet Networking',
                    description='Duis eleifend molestie leo at mollis sanctus intro.',
                    order=1,
                ),
            ])

        if not CounterStat.objects.exists():
            CounterStat.objects.bulk_create([
                CounterStat(icon_class='flaticon-dashboard', value=8792, label='Delivered Goods', order=0),
                CounterStat(icon_class='flaticon-customer-service', value=5463, label='IT Consultant', order=1),
                CounterStat(icon_class='flaticon-photo-editing', value=6535, label='Project Complete', order=2),
                CounterStat(icon_class='flaticon-productivity', value=7346, label='Fully Launched', order=3),
            ])

        if not Service.objects.exists():
            services = [
                ('Design Review', 'Web Development', 'images/resource/service-4.jpg'),
                ('Cloud Service', 'Data Analytics', 'images/resource/service-5.jpg'),
                ('Machine Learn', 'Mobile Development', 'images/resource/service-6.jpg'),
                ('Software Development', 'Web Development', 'images/resource/service-7.jpg'),
            ]
            for i, (title, category, img) in enumerate(services):
                Service.objects.create(title=title, category=category, static_image=img, order=i)

        if not TeamMember.objects.exists():
            members = [
                ('Monica Mora', 'Managing Director', 'images/resource/team-5.jpg'),
                ('Homer Donnie', 'Managing Director', 'images/resource/team-6.jpg'),
                ('Aalia Danial', 'Managing Director', 'images/resource/team-7.jpg'),
                ('Endi Morales', 'Managing Director', 'images/resource/team-8.jpg'),
            ]
            for i, (name, role, img) in enumerate(members):
                TeamMember.objects.create(
                    name=name, role=role, static_image=img, order=i,
                    facebook_url='https://www.facebook.com/',
                    twitter_url='https://www.twitter.com/',
                )

        if not Project.objects.exists():
            projects = [
                ('IT Solution Plan', 'Technology', 'images/gallery/7.jpg'),
                ('Design Review', 'Technology', 'images/gallery/8.jpg'),
                ('UGACloud Analysis', 'Technology', 'images/gallery/9.jpg'),
                ('Machine Learning', 'Technology', 'images/gallery/11.jpg'),
                ('Software Renew', 'Technology', 'images/gallery/10.jpg'),
                ('Enterprise Platform', 'Technology', 'images/gallery/12.jpg'),
            ]
            for i, (title, category, img) in enumerate(projects):
                Project.objects.create(title=title, category=category, static_image=img, order=i)

        if not Testimonial.objects.exists():
            Testimonial.objects.create(
                quote=(
                    'UGACloud analysts have done an excellent job presenting the analysis & insights. '
                    'We are confident that they have helped move our business.'
                ),
                author_name='Franklin Sinatran',
                author_role='Assistant Manager',
            )

        if not BlogPost.objects.exists():
            BlogPost.objects.create(
                title='Define World IT Solution Technology',
                author='Michael K. Staven',
                published_date=date(2021, 5, 15),
                excerpt='Lorem ipsum dolor sit amet, consectetur adipiscing elit looking at its layout',
                body='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Full article content goes here.',
                static_image='images/resource/news-7.jpg',
                is_featured=True,
            )
            BlogPost.objects.create(
                title='App Promotes Sales and Profits In IT Solutions',
                author='Michael K. Staven',
                published_date=date(2021, 5, 15),
                excerpt='Lorem ipsum dolor sit amet, consectetur adipiscing elit looking at its layout',
                body='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Full article content goes here.',
                static_image='images/resource/news-1.jpg',
            )
            BlogPost.objects.create(
                title='In Depth Industry and Ecosystem Analysis',
                author='Michael K. Staven',
                published_date=date(2021, 5, 10),
                excerpt='Lorem ipsum dolor sit amet, consectetur adipiscing elit looking at its layout',
                body='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Full article content goes here.',
                static_image='images/resource/news-2.jpg',
            )

        if not ClientLogo.objects.exists():
            for i, num in enumerate([1, 2, 3, 4, 5], start=0):
                ClientLogo.objects.create(
                    name=f'Client {num}',
                    static_image=f'images/clients/{num}.png',
                    order=i,
                )

        if not Download.objects.exists():
            Download.objects.bulk_create([
                Download(
                    title='Software',
                    subtitle='Best Document-Sharing Software',
                    file_size_label='Download (2.5 mb)',
                    order=0,
                ),
                Download(
                    title='Statement',
                    subtitle='Get Your Free Consulting Invoice',
                    file_size_label='Download (3.5 mb)',
                    order=1,
                ),
            ])

        LegalPage.objects.update_or_create(
            slug='terms',
            defaults={
                'title': 'Terms of Use',
                'content': (
                    'These terms govern your use of our website and services. '
                    'By accessing this site you agree to comply with all applicable laws and regulations.'
                ),
            },
        )
        LegalPage.objects.update_or_create(
            slug='privacy',
            defaults={
                'title': 'Privacy Policy',
                'content': (
                    'We respect your privacy and are committed to protecting your personal data. '
                    'This policy explains how we collect, use, and safeguard your information.'
                ),
            },
        )

        headings = [
            ('home', 'counters', 'NUMBERS ARE TALKING', "Let's Talk About Our Business Growth in IT Consulting Solution"),
            ('home', 'services', 'OUR SERVICE', 'We Provide Best Solutions For Preparing Your Success Business',
             'We help digital companies to volume their self-interest and get a space.'),
            ('home', 'team', 'TEAM MEMBERS', 'People Behind Our Success Team Members'),
            ('home', 'projects', 'Our latest Projects', 'Check Now Our Successful Team Work'),
            ('home', 'testimonials', "OUR CLIENT'S REVIEW", 'What Client Say About Us?'),
            ('home', 'blog', 'latest news & artical', 'You Get Every Single Update For You',
             'Lorem ipsum dolor amet consectetur adips elit sed do eiusmod tempor incididunt.'),
            ('team', 'main', '', 'Expert Team Person'),
            ('team', 'grid', 'TEAM MEMBERS', 'People Behind Our Success Team Members'),
            ('projects', 'main', '', 'Our Projects'),
            ('blog', 'main', '', 'Our Blog'),
            ('contact', 'main', '', 'Contact Us'),
        ]
        for item in headings:
            page, key, eyebrow, title = item[:4]
            desc = item[4] if len(item) > 4 else ''
            SectionHeading.objects.update_or_create(
                page=page,
                section_key=key,
                defaults={'eyebrow': eyebrow, 'title': title, 'description': desc},
            )

        self.stdout.write(self.style.SUCCESS('Site content seeded successfully.'))
