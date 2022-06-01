from dataclasses import field
from logging import PlaceHolder
from pyexpat import model
from django.forms import EmailInput, ModelForm, PasswordInput, TextInput
from .models import Users

class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['name', 'surname', 'email', 'pasword']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control mt-2 mb-3',
                'placeholder': 'Enter your name'
            }),
            
            "surname": TextInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Enter your surname'
            }),
            
            "email": EmailInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Enter your email'
            }),
            
            "pasword": PasswordInput(attrs={
                'class': 'form-control mb-3',
                'placeholder': 'Enter your password'
            })

        }
            