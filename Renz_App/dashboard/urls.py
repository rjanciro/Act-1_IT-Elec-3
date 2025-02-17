from django.urls import path
from .views import dashboard, reports, settings

app_name = "dashboard"

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('reports/', reports, name='reports'),
    path('settings/', settings, name='settings'),
] 