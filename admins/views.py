from django.shortcuts import redirect, render

# Create your views here.
def admin_home(request):
    try:
        userid=request.session.get('userid')
        if userid == None:
            return redirect('error_404')
        return render(request,'admin/home.html')
    except Exception as e:
        userid = request.session.get('userid')
        print('Exception user_pymts', e)
        contexts = {'username': userid}
        return render(request, 'admin/home.html', contexts)