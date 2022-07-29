from django.urls import path

from . import views


urlpatterns = [
path('', views.index, name='index'),
path('profile/', views.profile, name='profile'),
path('profile/', views.update_profile, name='update_profile'),
 path("post/save/", views.create_post, name="save_post"),
path('signup/', views.signup, name='signup'),
path('login/', views.login, name='login')
]