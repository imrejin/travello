from . import views
from django.urls import path
from .views import about

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
]
