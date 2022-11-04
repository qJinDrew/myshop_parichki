from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),          #обращаемся к даннному методу
    path('detail/', views.detail, name='detail')
]

