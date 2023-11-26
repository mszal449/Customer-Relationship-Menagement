from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddLeadForm
from .models import Agent, Lead


def home(request):
    if request.user.is_authenticated:
        # Get agent for user and load leads
        agent = Agent.objects.get(user=request.user)
        leads = Lead.objects.filter(agent=agent)

        # Return message if there are no leads
        if not leads:
            messages.error(request, 'There are no leads to load...')
            return render(request, 'home.html', {})

        # Render leads
        return render(request, 'home.html', {'leads': leads})
    else:
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
            # Create and login user
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            # Create new Agent
            Agent.objects.create(user=user)

            messages.success(request, 'You have been succesfully registered!')
            return redirect('home')
    else:
        # Else return new form
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


def add_lead(request):
    # If request is "POST" type, form has been submitted
    if request.method == 'POST':
        form = AddLeadForm(request.POST)
        if form.is_valid():
            # If the form is valid, add current agent and save
            new_lead = form.save(commit=False)
            current_agent = Agent.objects.get(user=request.user)
            new_lead.agent = current_agent
            new_lead.save()

            messages.success(request, 'Succesfully saved the lead.')
            return redirect('home')
        else:
            # Else render form again with error messages
            return render(request, 'add_lead.html', {'form': form})
    else:
        # Else create new form
        form = AddLeadForm()
        return render(request, 'add_lead.html', {'form': form})
