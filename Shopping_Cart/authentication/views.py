from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages


# Create your views here.
from .forms import SignupFrom, SigninForm


def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful, enjoy the website")
                return redirect('index')
            else:
                messages.error(request, "Username or password is invalid")
        except Exception as e:
            messages.error(request, e)
    else:
        form = SigninForm()

    return render(request, 'authentication/signin.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration Completed')
            return redirect('signin')
        else:
            messages.error(request, "show the blow errors")

    else:
        form = SignupFrom()
    return render(request, 'authentication/signup.html', {'form': form})


def signout(request):
    logout(request)
    messages.success(request, "Signout successful")
    return redirect('signin')

