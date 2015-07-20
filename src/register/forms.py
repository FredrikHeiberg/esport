from django import forms

from .models import Join

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Join
        # Choose what fields to include in the form displayed at the page
        fields = ['first_name','last_name','email','address','zipcode','area',]