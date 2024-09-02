from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_view, name='search_view'),
    path('dashboard/', views.dashboard, name='dashboard'),
]