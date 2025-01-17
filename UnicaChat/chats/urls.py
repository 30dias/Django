from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.rooms_view, name='rooms'),
]