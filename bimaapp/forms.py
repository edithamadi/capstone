from django import forms
from.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        
        widgets = {
            'bio': forms.TextInput(attrs={'placeholder': 'Bio'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            }
        exclude = ['user', 'last_name']

class UserForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProposerForm(forms.ModelForm):
    class Meta:
        model = Proposer
        fields = ['first_name','surname', 'title', 'dateofbirth', 'id_number', 'maritalstatus', 'cellphone', 'emailaddress', 'relationshiptoassured']

class LifeassuredForm(forms.ModelForm):
    class Meta:
        model = Lifeassured
        fields = ['first_name','surname', 'title', 'dateofbirth', 'nationality', 'country', 'agelastbirthday', 'maritalstatus', 'sex']       

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['residentialname','workaddress', 'businessemail']   

class OccupationForm(forms.ModelForm):
     class Meta:
        model = Occupation
        fields = ['occupationname','annualincome']

class PremiumpaymethodForm(forms.ModelForm):
    class Meta:
        model = Premiumpaymethod
        fields = ['name','paymethod']       

class Bankers_OrderForm(forms.ModelForm):
    class Meta:
        model = Bankers_Order
        fields = ['bank_name','branch_name','account_name', 'account_number']       

