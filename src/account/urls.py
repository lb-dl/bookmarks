from django.urls import path
from . import views


urlpatterns = [
# post views
path('login/', views.UserLogin, name='login'),
]
