from django.urls import path
from admins import views  

urlpatterns = [
    path('admin_home/',views.admin_home,name='admin_home')
]