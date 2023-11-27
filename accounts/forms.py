from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Se requiere que ingrese una dirección de email válida')

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['image', 'username', 'email', 'description', 'website']
