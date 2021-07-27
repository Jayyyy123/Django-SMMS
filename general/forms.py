from django.db.models.base import Model
from general.models import MaintenanceRequest
from django.forms import ModelForm, TextInput, Textarea, Select
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateMaintenanceRequest(ModelForm):
    class Meta:
        model = MaintenanceRequest
        fields = ['hostel', 'category', 'progress', 'remark']
        widgets = {
            'hostel': TextInput(attrs={
                'class': "control",
                'style': 'width: 100%; border: 1px solid #03071e; outline: none;',
            }),
            'category': Select(attrs={
                'class': "select is-fullwidth",
                'style': 'border: 1px solid  #03071e; outline: none;',
            }),
            'progress': Select(attrs={
                'class': "select is-fullwidth",
                'style': 'border: 1px solid #03071e; outline: none;',
            }),
            'remark': Textarea(attrs={
                'class': "textarea",
                'style': 'width: 100%; border: 1px solid #03071e; outline: none;',
            }),
        }
