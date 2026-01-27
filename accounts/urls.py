from django.urls import path
from .views import register_view, logout_view, dashboard

urlpatterns = [
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard')
]
