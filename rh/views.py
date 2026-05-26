from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import InscriptionForm, ConnexionForm, ProfilForm, CongeForm
from .models import Employe, Conge, Service

# Inscription

def inscription(request):
    form = InscriptionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            groupe = Group.objects.get(name='Employé')
            user.groups.add(groupe)
            login(request, user)
            return redirect('dashboard')
    return render(request, 'rh/inscription.html', {'form': form})
# connexion
def connexion(request):
    form = ConnexionForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                from .models import User
                user_obj = User.objects.get(email=email)
                user = authenticate(request, username=user_obj.email, password=password)
                if user:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    form.add_error(None, 'Mot de passe incorrect')
            except:
                form.add_error(None, 'Email introuvable')
    return render(request, 'rh/connexion.html', {'form': form})

# Déconnexion
@login_required
def deconnexion(request):
    logout(request)
    return redirect('connexion')

# Dashboard
@login_required
def dashboard(request):
    return render(request, 'rh/dashboard.html')

# Profil
@login_required
def profil(request):
    if request.method == 'POST':
        form = ProfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profil')
    else:
        form = ProfilForm(instance=request.user)
    return render(request, 'rh/profil.html', {'form': form})

@login_required
def demande_conge(request):
    try:
        employe = request.user.employe
    except:
        return redirect('dashboard')
    form = CongeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            conge = form.save(commit=False)
            conge.employe = employe
            conge.save()
            return redirect('conge_list')
    return render(request, 'rh/demande_conge.html', {'form': form})

# Liste des employés
class EmployeListView(LoginRequiredMixin, ListView):
    model = Employe
    template_name = 'rh/employe_list.html'
    context_object_name = 'employes'
    paginate_by = 10

# Liste des congés
class CongeListView(LoginRequiredMixin, ListView):
    model = Conge
    template_name = 'rh/conge_list.html'
    context_object_name = 'conges'
    paginate_by = 10

# Create your views here.
