from django.urls import path
from superadmin import views  

urlpatterns = [
    path('superadmin_dashboard/',views.superadmin_dashboard,name='superadmin_dashboard')
]