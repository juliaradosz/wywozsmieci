from django.urls import path

from . import views

urlpatterns = [
    path('', views.harmonogram, name='harmonogram'),
    path('dodaj/', views.dodaj, name='dodaj'),
    path('edytuj/<int:pk>/', views.edytuj, name='edytuj'),
    path('usun/<int:pk>/', views.usun, name='usun'),
    path('lista/', views.lista, name='lista'),
]
