from django.urls import path
from Resume import views

urlpatterns = [
    path('', views.about_me, name='about-me'),
]