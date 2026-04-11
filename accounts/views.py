from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.contrib.auth.models import User

def account_main_view(request):
    return render(request, 'accounts/account-main.html', {'data': ''})


def registration_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            context = {'account': user}
            return render(request, 'accounts/partials/profile.html', context)
    context = {'form': UserCreationForm()}
    return render(request, 'accounts/partials/register.html', context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            context = {'account': user}
            return render(request, 'accounts/partials/profile.html', context)
    context = {'form': AuthenticationForm()}
    return render(request, 'accounts/partials/login.html', context)

def logout_view(request):
    logout(request)
    return render(request, 'accounts/partials/login.html', {'form': AuthenticationForm()})

def delete_account_view(request):
    user = request.user
    user.delete()
    return HttpResponse("")