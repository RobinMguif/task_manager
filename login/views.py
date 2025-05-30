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
            sa = super_admin.objects.get(username=username, password=password)
            request.session['userid'] = sa.id
            # return HttpResponse(userid)
            print(sa)  # Debug log
            return redirect('superadmin_dashboard')
        except super_admin.DoesNotExist:
            print('No matching super_admin')  # Debug log
            messages.error(request, 'Invalid username or password')
        except Exception as e:
            print(f"Unexpected error: {e}")  # Helpful for catching other issues

    return render(request, 'login.html')

def error_404(request):
    return render(request,'404.html')