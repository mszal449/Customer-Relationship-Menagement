from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import AddLeadForm, FilterLeadsForm
from crm.models import Agent, User
from .models import Lead


# Home page
def home(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # If the user is authenticated, render home page
        return render(request, '../crm/templates/home.html', {})
    else:
        # If not, redirect to login page
        return redirect('login')


# Login site
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
                return redirect('home')
        else:
            # If it is not a POST request, render the home page
            return render(request, '../crm/templates/home.html', {})


# Leads
def leads(request):
    form = FilterLeadsForm(request.GET, user=request.user)  # Pass the currently logged-in user to the form
    leads_result = Lead.objects.all()

    if request.GET and form.is_valid():
        # Apply filters based on form data
        if form.cleaned_data['name']:
            leads_result = leads_result.filter(name__icontains=form.cleaned_data['name'])
        if form.cleaned_data['surname']:
            leads_result = leads_result.filter(surname__icontains=form.cleaned_data['surname'])
        if form.cleaned_data['email']:
            leads_result = leads_result.filter(email__icontains=form.cleaned_data['email'])
        if form.cleaned_data['phone_number']:
            leads_result = leads_result.filter(phone_number__icontains=form.cleaned_data['phone_number'])
        if form.cleaned_data['agent']:
            leads_result = leads_result.filter(agent=form.cleaned_data['agent'])

    return render(request, 'leads.html', {'leads': leads_result, 'form': form})


def lead(request, pk):
    # Check user authorization
    if request.user.is_authenticated:
        try:
            # Retrieve lead data based on provided ID and associated agent model
            searched_lead = get_users_lead(request, pk)
        except Lead.DoesNotExist:
            messages.error(request, 'Lead not found')
            return redirect('leads')

        # Render lead website with lead data
        return render(request, 'lead.html', {'lead': searched_lead})

    # If user is not authorized, redirect to the home page
    return redirect('home.html')


def add_lead(request):
    # Check if the form has been submitted (POST request)
    if request.method == 'POST':
        # Bind submitted form data from to the form
        form = AddLeadForm(request.POST)
        if form.is_valid():
            # If the form is valid, save the lead with the current agent
            new_lead = form.save(commit=False)
            new_lead.agent = get_current_agent(request)
            new_lead.save()

            # Inform the user about successful lead creation
            messages.success(request, 'Succesfully saved the lead.')

            # Redirect the user to the leads page
            return redirect('leads')
        else:
            # If the form is not valid, render the form with error messages
            return render(request, 'add_lead.html', {'form': form})
    else:
        # If it is not a POST request, create an empty form
        form = AddLeadForm()

        # Render the form page with empty form
        return render(request, 'add_lead.html', {'form': form})


def update_lead(request, pk):
    # Check user authentication
    if request.user.is_authenticated:
        # If the user is authenticated, get the lead object associated with the user
        found_leads = get_users_lead(request, pk)

        # Check if the lead exists
        if found_leads is None:
            messages.error(request, 'Lead not found.')
            return redirect('leads')

        # Create a form filled with lead information
        form = AddLeadForm(request.POST or None, instance=found_leads)

        if request.method == 'POST':
            if form.is_valid():
                # If the form is valid, save the changes
                form.save()
                messages.success(request, 'Lead information has been successfully updated.')

                # Redirect to the lead details page
                return redirect('lead', pk=found_leads.pk)

            # If the form is not valid, render the page with errors
            messages.error(request, 'Form is not valid. Please correct the errors.')

        # Render the update_lead page with the form
        return render(request, 'update_lead.html', {'form': form, 'lead': found_leads})
    else:
        messages.success(request, "You must be logged in to perform this action.")
        return redirect('home')


def delete_lead(request, pk):
    # Check user authentications
    if request.user.is_authenticated:
        # Retrieve the current agent associated with the request
        agent = get_current_agent(request)

        try:
            # Attempt to find the lead based on provided ID and associated agent
            searched_lead = Lead.objects.get(id=pk, agent=agent)
        except Lead.DoesNotExist:
            messages.error(request, 'Lead not found')
            return redirect('leads')

        # Delete the lead if found
        searched_lead.delete()

        # Inform the user about succesful deletion
        messages.success(request, 'Lead has been successfully deleted.')

        # Redirect the user back to the leads page
        return redirect('leads')
    else:
        # If user is not authenticated, redirect them to the home page
        return redirect('home')


def get_current_agent(request):
    if request.user.is_authenticated:
        # If user is logged in, retrieve agent object associated with logged-in user
        agent = Agent.objects.get(user=request.user)
        return agent

    # If user is not authenticated, return None
    return None


def get_users_lead(request, id):
    agent = get_current_agent(request)

    try:
        # Try retrieving lead based on given ID and user associated agent object
        searched_lead = Lead.objects.get(id=id, agent=agent)

        # Return found lead
        return searched_lead
    except Lead.DoesNotExist:
        raise


# Statistics
def stats(request):
    if request.user.is_authenticated:
        return render(request, 'stats.html', {})
    else:
        return redirect('login')
