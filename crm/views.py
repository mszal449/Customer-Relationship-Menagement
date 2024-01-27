from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Agent


# Home page
def home(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # If the user is authenticated, render home page
        return render(request, 'home.html', {})
    else:
        # If not, redirect to login page
        return redirect('login')


# Login page
def login_user(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # If the user is authenticated, redirect to home page
        return redirect('home')
    else:
        # If user is not authenticated, check the type of the request
        if request.method == 'POST':
            # If it is a POST request, retrieve submited data for authentication
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Authenticate user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # If authentication is succesful, log in the user
                messages.success(request, 'Succesfuly logged in.')
                login(request, user)
                return redirect('home')
            else:
                # If authentication fails, redirect to the home page with an error message
                messages.error(request, 'Authentication failed, please try again.')
                return redirect('login')
        else:
            # If it is not a POST request, render the home page
            return render(request, 'login.html', {})


# Register Page
def register_user(request):
    # If request is “POST” type, form has been submitted
    if request.method == 'POST':
        # Create a form with request data
        form = SignUpForm(request.POST)

        # If form data is valid
        if form.is_valid():
            # Save form in the database
            form.save()

            # Authenticate user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            # Create new agent associated with user
            Agent.objects.create(user=user)

            messages.success(request, 'You have been succesfully registered!')
            return redirect('home')
    else:
        # Else return an empty form
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


# Authorization
def logout_user(request):
    # Log out current user
    logout(request)

    # Inform the user about the succusful logout
    messages.success(request, 'You have been logged out')

    # Redirect the user to the home page
    return redirect('login')

