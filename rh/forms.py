from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Conge, User

class InscriptionForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'nom', 'prenom', 'password2']

class ConnexionForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class ProfilForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nom', 'prenom', 'adresse', 'photo']


class CongeForm(forms.ModelForm):
    class Meta:
        model = Conge
        fields = ['date_debut', 'date_fin', 'motif']
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'motif': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            }
        