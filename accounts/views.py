from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm, UserProfileForm
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('base.html')  
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('base.html') 
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def view_profile(request):
    return render(request, 'profile.html', {'user': request.user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def delete_profile(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('base.html') 
    return render(request, 'delete_profile.html')
