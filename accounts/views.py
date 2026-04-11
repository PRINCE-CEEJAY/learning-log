from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render

# Create your views here.
def registration_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            account = form.save()
            context = {'account': account}
            return render(request, 'accounts/partials/profile.html', context)
    context = {'form': UserCreationForm()}
    return render(request, 'account/partials/register.html', context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            context = {'account': user}
            return render(request, 'account/partials/profile.html', context)
    context = {'form': AuthenticationForm()}
    return render(request, 'account/partials/login.html', context)

def logout_view(request):
    user = AuthenticationForm(request.POST)
    logout(request, user)
    return render(request, 'account/partials/login.html')

def delete_account_view(request):
    account = get_object_or_404(user=request.user)
    account.delete()
    return HttpResponse("")