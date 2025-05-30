from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from superadmin.models import user_admin





# Create your views here.
def superadmin_dashboard(request):
    try:
        userid=request.session.get('userid')
        if userid == None:
            return redirect('error_404')
        return render(request,'superadmin/dashboard.html')
    except Exception as e:
        userid = request.session.get('userid')
        print('Exception user_pymts', e)
        contexts = {'username': userid}
        return render(request, 'superadmin/dashboard.html', contexts)






def user_view(request):
    try:
        userid=request.session.get('userid')
        if userid == None:
            return redirect('error_404')
        if request.method=='POST':
            name=request.POST.get('name')
            email=request.POST.get('email')
            phoneno=request.POST.get('phone')
            username=request.POST.get('username')
            password=request.POST.get('password')
            is_admin=request.POST.get('is_admin')
            add=user_admin()
            add.username=username
            add.password=password
            add.name=name
            add.email=email
            add.phoneno=phoneno
            add.is_admin=is_admin
            add.delete_status='0'
            add.save()
            messages.success(request,f'<strong>Sucessfully Added User</strong>')
            return redirect('user_view')
        users=user_admin.objects.filter(is_admin=0,delete_status=0)
        contexts={'userid':userid,'users':users}
        return render(request,'superadmin/user_view.html',contexts)
    except Exception as e:
        userid = request.session.get('userid')
        print('Exception user_pymts', e)
        contexts = {'username': userid}
        return render(request, 'superadmin/user_view.html', contexts)





def user_edit(request):
    if request.method=='POST':
        id=request.POST.get('user_id')
        is_admin=request.POST.get('is_admin')
        edit=user_admin.objects.get(id=id)
        edit.is_admin=is_admin
        edit.save()
        messages.success(request,f'<strong>Sucessfully Edited User</strong>')
        return redirect('user_view')





def view_admin(request):
    try:
        userid=request.session.get('userid')
        if userid == None:
            return redirect('error_404')
        if request.method=='POST':
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            username=request.POST.get('username')
            password=request.POST.get('password')
            is_admin=request.POST.get('is_admin')
            add=user_admin()
            add.name=name
            add.email=email
            add.phoneno=phone
            add.username=username
            add.password=password
            add.is_admin=is_admin
            add.delete_status=0
            add.save()
            messages.success(request,f'<strong>Sucessfully Add Admin</strong>')
            return redirect('view_admin')
        admin=user_admin.objects.filter(is_admin=1,delete_status=0)
        contexts={'admin':admin}
        return render(request,'superadmin/view_admin.html',contexts)
    except Exception as e:
        userid = request.session.get('userid')
        print('Exception user_pymts', e)
        contexts = {'username': userid}
        return render(request, 'superadmin/view_admin.html', contexts)
    
    
    
    
    
def delete_admin(request):
    if request.method=='POST':
        id=request.POST.get('user_id')
        delete=user_admin.objects.get(id=id)
        delete.delete_status='1'
        delete.save()
        messages.success(request,f'<strong>Deleted Successfully</strong>')
        return redirect('view_admin')
    
   
   
    
def delete_user(request):
    if request.method=='POST':
        id=request.POST.get('user_id')
        delete=user_admin.objects.get(id=id)
        delete.delete_status=1
        delete.save()
        messages.success(request,f'<strong>Deleted Successfully</strong>')
        return redirect('view_admin')