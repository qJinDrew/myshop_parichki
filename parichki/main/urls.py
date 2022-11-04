from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),          #обращаемся к даннному методу
    path('about', views.about, name='about'),     #при переход по .../about, переход к данному методу
    path('contacts', views.contacts, name='contacts'), #при переход по .../contacts, переход к данному методу
]
