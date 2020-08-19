from django import forms
from portfolio.models import MyUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
 
    class Meta:
        model = MyUser
        fields = ['username', "email"]

class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField()
 
    class Meta:
        model = MyUser
        fields = ['username', "email"]