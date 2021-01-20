from django.contrib.auth import views as auth_views
from django.urls import path

from . import views


urlpatterns = [
    # path('login/', views.UserLogin, name='login'),
    # use LoginView and LogOut views of Django's authentication framework
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
]
