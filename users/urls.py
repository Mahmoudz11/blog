from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import RedirectView

from . import views


urlpatterns = [
    path('', RedirectView.as_view(url='profile')),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', LoginView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', views.register_user, name='register'),
    path('profile/', views.profile_user, name='profile'),
    path('logout', views.logout_user, name='logout'),
]
