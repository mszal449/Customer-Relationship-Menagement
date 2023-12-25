import phonenumber_field.widgets
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from django import forms
from .models import User, Lead, Agent


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=50,
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    email = forms.EmailField(
        label='Email Address',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        max_length=50,
        label='First Name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=50,
        label='Last Name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}),
        help_text=
        '''<ul class="form-text text-muted small">
                <li>Your password can\'t be too similar to your other personal information.</li>
                <li>Your password must contain at least 8 characters.</li>
                <li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li>
            </ul>'''
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}),
        help_text=
        '''<span class="form-text text-muted">
                <small>Enter the same password as before, for verification.</small>
            </span>'''
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class AddLeadForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        label='Name',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    surname = forms.CharField(
        max_length=100,
        label='Surname',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    phone_number = PhoneNumberField(
        region=None,
        widget=phonenumber_field.widgets.RegionalPhoneNumberWidget(
            region=None,
            attrs={'class': 'form-control'}
        )
    )

    agent = forms.ModelChoiceField(
        queryset=Agent.objects.all(),
        label='Agent',
        widget=forms.Select(attrs={'class': 'form-control'})
    )


    class Meta:
        model = Lead
        fields = ['name', 'surname', 'email', 'phone_number', 'agent']


class FilterLeadsForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        label='Name',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False
    )
    surname = forms.CharField(
        max_length=100,
        label='Surname',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False

    )
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False

    )
    phone_number = PhoneNumberField(
        region=None,
        widget=phonenumber_field.widgets.RegionalPhoneNumberWidget(
            region=None,
            attrs={'class': 'form-control'}
        ),
        required=False
    )
    agent = forms.ModelChoiceField(
        queryset=Agent.objects.all(),
        label='Agent',
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = Lead
        fields = ['name', 'surname', 'email', 'phone_number', 'agent']


