from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields

from userApp.models import Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    image = forms.ImageField(max_length=225,required=False )
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','image' )
        help_texts = {
            'username': None,
            'email': None,
        }



class Userauth(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']
        help_texts = {
            'username': None,
            'email': None,
        }


class userProfileForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['name', 'phone', 'email', 'picture']


