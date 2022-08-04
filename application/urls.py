from django.urls import path

from . import views


urlpatterns = [
path('', views.index, name='index'),
path('profile/', views.profile, name='profile'),
path('profile/', views.update_profile, name='update_profile'),
path('posts/', views.posts, name='posts'),
path("post/save/", views.create_post, name="save_post"),
path('signup/', views.authentication, name='authentication'),
]