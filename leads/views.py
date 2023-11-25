from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # Check if the request is a POST request
    if request.method == 'POST':
        # If it is, the user is trying to login
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Try authenticating
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login user if authentication is succesful
            messages.error(request, 'Succesfuly logged in.')
            login(request, user)
            return redirect('home')
        else:
            # Redirect to login page to reset the form
            messages.error(request, 'Authentication failed, please try again.')
            return redirect('home')
    else:
        # If user is authenticated, render home page
        return render(request, 'home.html', {})
