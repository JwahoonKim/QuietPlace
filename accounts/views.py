import accounts
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth  # 추가
from accounts.models import Profile
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['re_password']:
            user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password'])
            user.profile.nickname = request.POST['nickname']
            user.profile.email = request.POST['email']
            user.profile.profile_pic = request.POST['profile_pic']
            auth.login(request, user,
                       backend='django.contrib.auth.backends.ModelBackend')
            user.profile.save()
            return redirect('/')
    return render(request, 'accounts/signup.html')


def revise(request):
    if request.method == 'POST':
        Profile.objects.filter(user=request.user).update(
            nickname=request.POST['nickname'])
        return redirect('/posts/my_page')

    return render(request, 'accounts/revise.html')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})
