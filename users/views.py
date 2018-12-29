from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .forms import UserRegisterForm, UserUpdateForm


def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfuly')
            return redirect('user:login')
        else:
            return messages.error(request, 'something not correct please check again!')
    form = UserRegisterForm()
    context = {
        'form':form
    }
    return render(request, 'users/register.html', context)

@login_required
def profile_user(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        # p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() :#and p_form.is_valid():
            u_form.save()
            # p_form.save()
            messages.success(request, 'Profile updated!')
            return redirect('user:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        # p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form':u_form,
        # 'p_form':p_form
    }
    return render(request, 'users/profile.html', context)


def logout_user(request):
    logout(request)
    return render(request, 'users/logout.html')
