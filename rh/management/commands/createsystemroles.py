from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from rh.models import Conge, User

class Command(BaseCommand):
    help = 'crée les rôles système et leur affecte les permissions natives'

    def handle(self, *args, **options):
        conge_type = ContentType.objects.get_for_model(Conge)
        user_type = ContentType.objects.get_for_model(User)

        can_add_conge = Permission.objects.get(codename="add_conge", content_type=conge_type)
        can_change_conge = Permission.objects.get(codename="change_conge", content_type=conge_type)
        can_view_conge = Permission.objects.get(codename="view_conge", content_type=conge_type)
        can_view_users = Permission.objects.get(codename="view_user", content_type=user_type)
        can_change_users = Permission.objects.get_or_create(codename="change_user",content_type=user_type)

        role_permission = {
            'Employé': [can_add_conge, can_view_conge], 
            'Manger':[can_view_conge, can_view_users], 
            'RH': [can_view_conge, can_change_conge, can_view_users, can_change_users],
            }
        for role,Permission in roles_permission.items(): # type: ignore
            group, created = Group.objects.get_or_create(name=role)
            group.permissions.set(Permission)
            if created:
                self.stdout.write(f'✅ Rôle "{role}" créé avec ses permissions.')
            else:
                self.stdout.write(f'⚠️ Rôle "{role}" mis à jour.')
        # return super().handle(*args, **options)