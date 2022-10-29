from django.urls import path
from AppPlayground import views

urlpatterns = [
    path('', views.inicio),
]
