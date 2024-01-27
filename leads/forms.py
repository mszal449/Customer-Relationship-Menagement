from django import forms
from phonenumber_field.formfields import PhoneNumberField
import phonenumber_field.widgets
from .models import Lead
from crm.models import Agent


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

    # Set defualt agent as currently logged in agent
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(FilterLeadsForm, self).__init__(*args, **kwargs)

        if user and user.is_authenticated:
            agent = Agent.objects.filter(user=user).first()
            if agent:
                self.fields['agent'].initial = agent
                print(self.fields['agent'].initial)

    class Meta:
        model = Lead
        fields = ['name', 'surname', 'email', 'phone_number', 'agent']


