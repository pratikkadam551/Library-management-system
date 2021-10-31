from django import forms
from django.contrib.auth.models import User
from .models import Books
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm,UsernameField



class Signupform(forms.Form):
    username = forms.CharField(label='Username', max_length=100, min_length=2,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First name', max_length=100, min_length=2,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last name', max_length=100, min_length=2,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=20, min_length=2,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', max_length=50, min_length=2,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password',
                                max_length=50, min_length=2,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
class Loginform(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


class Bookform(forms.ModelForm):
    class Meta:
        model=Books
        fields=['id','title','description']
        # label={'title':'Title','desc':'Desc'}
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
                 'description':forms.Textarea(attrs={'class':'form-control'})
                 }
