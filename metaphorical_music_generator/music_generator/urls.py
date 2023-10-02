from django.urls import path
from . import views

urlpatterns = [
    path('generate_music/', views.generate_music, name='generate_music'),
]
