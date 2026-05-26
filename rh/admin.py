from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Employe, Service, Conge

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'nom', 'prenom', 'is_staff']
    ordering = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Infos', {'fields': ('nom', 'prenom', 'adresse', 'date_naissance', 'photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
    )
    add_fieldsets = (
        (None, {
            'fields': ('email', 'nom', 'prenom', 'password1', 'password2'),
        }),
    )

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['nom']

@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ['user', 'poste', 'date_embauche']

@admin.register(Conge)
class CongeAdmin(admin.ModelAdmin):
    list_display = ['employe', 'date_debut', 'date_fin', 'statut']
    list_filter = ['statut']
    list_editable = ['statut']