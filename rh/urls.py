from django.urls import path
from .import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('profil/', views.profil, name='profil'),
    path('employes/', views.EmployeListView.as_view(), name='employe_list'),
    path('conges/', views.CongeListView.as_view(), name='conge_list'),
    path('conges/demande/', views.demande_conge, name='demande_conge'),
    ]