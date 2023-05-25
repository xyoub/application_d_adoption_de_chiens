from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Utilisateur
# from .models import Product


class InscriptionForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}))

    class Meta:
        model = Utilisateur
        fields = ['username', 'nom', 'prenom', 'tel', 'gmail', 'password']
        help_texts = {
            'username': '', #Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only 
            'nom':'',
        }
        widgets = {
            'username': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'}),
            'nom': TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'prenom': TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'tel': TextInput(attrs={'class': 'form-control', 'placeholder': 'Numéro de téléphone'}),
            'gmail': TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

class ConnexionForm(AuthenticationForm):
    username = forms.CharField(label="Username:", widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}))
    # help_texts = {
    #     'username': 'fddfdffd', # Help text for the username field
    #     'nom': '',  # No help text specified for the 'nom' field
    # }



# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name', 'description', 'image']

