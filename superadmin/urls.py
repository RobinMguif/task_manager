from django.urls import path
from superadmin import views  

urlpatterns = [
    path('superadmin_dashboard/',views.superadmin_dashboard,name='superadmin_dashboard'),
    path('user_view/',views.user_view,name='user_view'),
    path('user_edit',views.user_edit,name='user_edit'),
    path('view_admin/',views.view_admin,name='view_admin'),
    path('delete_admin',views.delete_admin,name='delete_admin'),
    path('delete_user',views.delete_user,name='delete_user')
]