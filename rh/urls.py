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
    path('equipe', views.TeamByServiceListView.as_view(), name='equipe_par_service'),

    path('conges/historique/', views.MonHistoriqueCongeListView.as_view(), name='mon_historique_conges'),
    path('conges/traiter/<int:pk>/<str:action>/', views.ProcessCongeView.as_view(), name='traiter_conge'),
    path('profil/changement-mot-de-passe/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('profil/changement-mot-de-passe/succes/', views.CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
    ]