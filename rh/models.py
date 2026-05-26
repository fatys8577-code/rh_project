from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email obligatoire')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255, blank=True)
    date_naissance = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['prenom','nom']
    objects = UserManager()

    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
class Service(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Employe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    poste = models.CharField(max_length=100)
    date_embauche = models.DateField()

    def __str__(self):
        return str(self.user)
    
class Conge(models.Model):
    STATUT_CHOIX = [
        ('en_attente', 'En attente'),
        ('approuve', 'Approuvé'),
        ('rejete', 'Rejeté'),
        ]
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    motif = models.TextField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOIX, default='en_attente')
    date_demande = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Congé de{self.employe} - {self.statut}"


# Create your models here.
