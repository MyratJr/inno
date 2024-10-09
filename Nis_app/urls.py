# nis_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:lg>', views.home, name='home'),
    path('country/<int:pk>/<str:lg>', views.country_detail, name='country_detail'),
    path('about-theme/<str:lg>', views.about_theme, name='about_theme'),
    path('message/<str:lg>', views.message, name='message'),
    path('success/', views.success_view, name='success'),
]
