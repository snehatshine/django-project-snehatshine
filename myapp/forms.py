from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["username","email","phone","role","password"]
        widgets = {
            "username": forms.TextInput(),
            "email": forms.EmailInput(),
            "phone": forms.TextInput(),
            "role": forms.Select(),
            "password": forms.PasswordInput(),
        }