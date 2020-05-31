from django import forms
from django.forms import ModelForm

from .models import UserProfile

# Create the form class.
USER_CHOICES = (
    ("buyer", "Buyer"),
    ("seller", "Seller"),
)

STATE_CHOICES = (
    ("Madhya Pradesh", "Madhya Pradesh"),
    ("Hyderabad", "Hyderabad"),
    ("Mumbai", "Mumbai"),
    ("Delhi", "Delhi"),
    ("Gujarat", "Gujarat"),

)


class UserRegistrationForm(ModelForm):
    name = forms.CharField(max_length=20, required=True)
    # last_name = forms.CharField(max_length=20, required=True)
    email = forms.CharField(max_length=20, required=True)
    # password = forms.CharField(max_length=20, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    user_type = forms.CharField(max_length=20, widget=forms.Select(choices=USER_CHOICES), )
    state = forms.CharField(max_length=20, widget=forms.Select(choices=STATE_CHOICES), )

    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'password', 'user_type', 'phone_number', 'address',
                  'country', 'state', 'zip_code']
        exclude = ('is_active', 'is_staff')
