from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('dash/<userEnterdUsername>', views.dashboard, name = 'dashboard'),
]