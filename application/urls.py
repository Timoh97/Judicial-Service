from django.urls import path

from . import views


urlpatterns = [
path('', views.index, name='index'),
path('profile/', views.profile, name='profile'),
path('profile/', views.update_profile, name='update_profile'),
path('post/', views.post, name='post'),
path('services/', views.services, name='services'),
path('client/', views.client, name='client'),
path('contact/', views.contact, name='contact'),
path('about/', views.about, name='about'),
path("post/save/", views.create_post, name="save_post"),
path('signup/', views.authentication, name='authentication'),
]