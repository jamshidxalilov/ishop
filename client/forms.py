from django import forms
from .models import User
from django.core.exceptions import ValidationError
from ishop.widgets import ImageRenderWidget


class RegistrationForm(forms.ModelForm):
    confirm = forms.CharField(max_length=50, widget=forms.PasswordInput)

    def clean_confirm(self):
        if self.cleaned_data['confirm']!=self.cleaned_data['password']:
            raise ValidationError("Parollar bir xil bo'lishi shart.")

        return self.cleaned_data['confirm']
    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email', 'password', 'confirm')
        widgets = {
            'password': forms.PasswordInput
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'photo')
        widgets = {
            'photo': ImageRenderWidget
        }
