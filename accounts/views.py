import accounts
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth  # 추가


def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['re_password']:
            user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password'])
            user.profile.nickname = request.POST['nickname']
            auth.login(request, user)
            return redirect('/')
    return render(request, 'accounts/signup.html')

def revise(request):
    return render(request, 'accounts/revise.html')

def my_page(request):
    return render(request, 'accounts/my_page.html')
