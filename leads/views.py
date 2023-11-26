from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm


def home(request):
    # Check if the request is a POST request
    if request.method == 'POST':
        # If it is, the user is trying to login
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Try authenticating user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login user if authentication is succesful
            messages.success(request, 'Succesfuly logged in.')
            login(request, user)
            return redirect('home')
        else:
            # Redirect to login page to reset the form
            messages.error(request, 'Authentication failed, please try again.')
            return redirect('home')
    else:
        # If user is authenticated, render home page
        return render(request, 'home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return redirect('home')


def register_user(request):
    # If request is "POST" type, form has been submitted
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        # If form data is valid
        if form.is_valid():
            # Create user
            form.save()

            # Login user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have been succesfully registered!')
            return redirect('home')
    else:
        # Else return new form
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


