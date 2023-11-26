from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
from django.utils.safestring import mark_safe


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
        help_text=mark_safe(
            '''<ul class="form-text text-muted small">
                <li>Your password can\'t be too similar to your other personal information.</li>
                <li>Your password must contain at least 8 characters.</li>
                <li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li>
            </ul>''')
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}),
        help_text=mark_safe(
            '''<span class="form-text text-muted">
                <small>Enter the same password as before, for verification.</small>
            </span>''')
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
