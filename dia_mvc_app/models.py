from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Dossier(models.Model):
    """Cet objet représente les dossier des patients."""
    #type = models.CharField(max_length=200, help_text='Edition du livre')
    utilsateur  = models.OneToOneField(User, on_delete = models.CASCADE,
    primary_key = True, help_text='')
    addresse = models.CharField(max_length=200, null=True,help_text='Numero, Rue')
    CIN = models.CharField(max_length=200, null=True, help_text='Numero, Rue')

    Diagnostic   = models.ForeignKey('Diagnostic', on_delete=models.SET_NULL, null=True)
    Consultation = models.ForeignKey('Consultation', on_delete=models.SET_NULL, null=True)
    Prescription = models.ForeignKey('Prescription', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        #return self.nom
        return 'Dossier de {0}'.format(self.utilsateur.username)
        #return '{0} ({1})'.format(self.id,self.book.title))

class Diagnostic(models.Model):
    """Cet objet représente les diagnostics des patients."""
    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        #return self.nom
        #return 'Dossier de {0}'.format(self.utilsateur.username)
        #return '{0} ({1})'.format(self.id,self.book.title))


class Consultation(models.Model):
    """Cet objet représente les consultations des patients."""
    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        #return self.nom
        #return 'Dossier de {0}'.format(self.utilsateur.username)
        #return '{0} ({1})'.format(self.id,self.book.title))

class Prescription(models.Model):
    """Cet objet représente les prescriptions des patients."""

    def __str__(self):
        """Cette fonction est obligatoirement requise par Django.
           Elle retourne une chaîne de caractère pour identifier l'instance de la classe d'objet."""
        #return self.nom
        #return 'Dossier de {0}'.format(self.utilsateur.username)
        #return '{0} ({1})'.format(self.id,self.book.title))