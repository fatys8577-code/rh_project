from pyexpat.errors import messages
from .models import Conge

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import InscriptionForm, ConnexionForm, ProfilForm, CongeForm
from .models import Employe, Conge, Service
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

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

User = get_user_model()

class TeamByServiceListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'rh/equipe_service.html'
    context_object_name = 'employes'
    paginate_by = 20  

    def get_queryset(self):
        return User.objects.filter(is_active=True).select_related('service').order_by('service__nom', 'last_name')


from django.shortcuts import get_object_or_404, redirect
from django.views import View
from .models import Conge  

class ProcessCongeView(View):
    def post(self, request, pk, action):
        # 1. On récupère le congé ou on renvoie une erreur 404 propre si inconnu
        conge = get_object_or_404(Conge, pk=pk)
        
        # 2. On change le statut selon l'action reçue en paramètre
        if action == 'approuver':
            conge.statut = 'approuve'
        elif action == 'rejeter':
            conge.statut = 'rejete'
            
        # 3. On sauvegarde les modifications en base de données
        conge.save()
        
        # 4. REDIRECTION PROPRE : On redirige directement vers l'URL de la liste
        return redirect('/conges/')

class MonHistoriqueCongeListView(LoginRequiredMixin, ListView):
    model = demande_conge
    template_name = 'rh/mon_historique_conges.html'
    context_object_name = 'mes_conges'
    paginate_by = 10

    def get_queryset(self):
        return demande_conge.objects.filter(user=self.request.user).order_by('-date_debut')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['solde_restant'] = self.request.user.solde_conge
        return context   


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'registration/changement_mot_de_passe.html'
    success_url = reverse_lazy('password_change_done')

    def form_valid(self, form):
        messages.success(self.request, "Votre mot de passe a été mis à jour avec succès !")
        return super().form_valid(form)

class CustomPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'registration/changement_mot_de_passe_succes.html'       