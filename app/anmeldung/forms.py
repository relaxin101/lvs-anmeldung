from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, get_user_model, password_validation
from django.utils.translation import gettext_lazy as _


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'birthdate', 'email', 'phone_no', 'schulung', 'couleurname', 'verbindung',
                  'reception', 'burschung', 'chargen', 'password1', 'password2', ]
        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
            'reception': forms.DateInput(attrs={'type': 'date'}),
            'burschung': forms.DateInput(attrs={'type': 'date'}),
        }
