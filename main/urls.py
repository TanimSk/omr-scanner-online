from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('show', views.show, name='show'),
    path('omrs', views.omrs, name='omrs'),
    path('about', views.about, name='about'),
    path('make-me-happy', views.support, name='make-me-happy'),
]
