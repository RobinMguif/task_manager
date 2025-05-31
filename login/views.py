from django.shortcuts import render, redirect
from django.http import HttpResponse
from superadmin.models import *
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f"Username: {username}, Password: {password}")  # Debug log

        try:
            # Check for SuperAdmin
            sa = super_admin.objects.get(username=username, password=password)
            request.session['userid'] = sa.id
            print('Logged in as SuperAdmin:', sa)
            return redirect('superadmin_dashboard')

        except super_admin.DoesNotExist:
            pass  # Continue to check for other roles

        try:
            # Check for Admin
            ad = user_admin.objects.get(username=username, password=password, is_admin=1)
            request.session['userid'] = ad.id
            print('Logged in as Admin:', ad)
            return redirect('admin_home')

        except user_admin.DoesNotExist:
            pass  # Continue to check for regular user

        try:
            # Check for regular User
            usr = user_admin.objects.get(username=username, password=password, is_admin=0)
            request.session['userid'] = usr.id
            print('Logged in as User:', usr)
            return redirect('user_dashboard')

        except user_admin.DoesNotExist:
            print('No matching user in any role')  # Debug log
            messages.error(request, 'Invalid username or password')

        except Exception as e:
            print(f"Unexpected error: {e}")  # Helpful for catching other issues
            messages.error(request, 'Something went wrong. Please try again.')

    return render(request, 'login.html')



def error_404(request):
    return render(request,'404.html')