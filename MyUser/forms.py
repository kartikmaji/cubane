from .models import MyUser,Channels,Message
from django import forms

class LoginForm(forms.ModelForm):        
    class Meta:
        model=MyUser
        fields=('username','password')

class SignupForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=MyUser
        fields=('email','username','firstname','lastname','password','password1',
              'mobile',
        )
        widgets = {
             'password': forms.PasswordInput(),
        }

class NewChannelForm(forms.ModelForm):
	class Meta:
		model=Channels
		fields=('name',)

class PostForm(forms.ModelForm):
    class Meta:
        model=Message
        fields=('message',)