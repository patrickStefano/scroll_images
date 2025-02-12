from django.urls import path
from . import views

urlpatterns = [
  path('', views.venu, name='venu'),
  path('galery/', views.galery, name='galery'),
  path('ajouter', views.ajouter, name='ajouter'),
  path('photo/<str:pk>/', views.photo, name='photo'),
]