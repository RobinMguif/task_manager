from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def superadmin_dashboard(request):
    return render(request,'superadmin/dashboard.html')