from .models import MyUser
from django import forms

class LoginForm(forms.ModelForm):        
    class Meta:
        model=MyUser
        fields=('username','password')
