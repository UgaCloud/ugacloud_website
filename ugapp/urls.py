from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('coming-soon/', views.coming_soon, name='coming_soon'),
    path('team/', views.team, name='team'),
    path('team/<slug:slug>/', views.team_detail, name='team_detail'),
    path('projects/', views.projects, name='projects'),
    path('projects/<slug:slug>/', views.project_detail, name='project_detail'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
]