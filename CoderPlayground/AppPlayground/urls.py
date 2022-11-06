from django.urls import path
from django.contrib import admin
from AppPlayground import views


urlpatterns = [
    path('', views.inicio),
    path('Hijo/', views.hijo),
    path('FormEscritorio', views.FormEscritorio,name='FormEscritorio')
]
