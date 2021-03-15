from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from typing import List
import datetime
import dateutil
from   .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')


def test(request):
    return render(request, 'profile/full-screen-table.html')



#from django.contrib.auth.mixins import LoginRequiredMixin

# to make sure that only logged-in users can access the view.
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):

    # Cherche le dossier de l'utilisateur
    dossierUtl = Dossier.objects.all().filter(utilsateur = request.user)


    try:
        dossierUtlnext = Dossier.objects.get(utilsateur = request.user)
        #dossierUtlnext = Dossier.objects.get(utilsateur = request.user)


        # Cherche la liste de diagnostics de l'utilisateur
        diagnostics_list = Diagnostic.objects.all().filter( dossier__in= dossierUtl)

        #dossierUtlnext = Dossier.objects.get(utilsateur = request.user)
        sex  = dossierUtlnext.sex
        #age  = int( (date.today() - dossierUtlnext.dateDeNaissance) // timedelta(days=365.2425) )


        context = {
            'dossier': dossierUtl,
            #'age': age,
            'sex': sex,
            'diagnostics': diagnostics_list,
        }

        return render(request, 'profile/index.html', context = context)

    except:
        context = {
        'dossier': 'error',
        #'age': 'error',
        'sex': 'error',
        'diagnostics': False,
        }
        return render(request, 'profile/index.html', context = context)


@login_required
def profileRendezVous(request):
    # Cherche le dossier de l'utilisateur
    dossierUtl = Dossier.objects.all().filter(utilsateur = request.user)

    try:
        dossierUtlnext = Dossier.objects.get(utilsateur = request.user)
        #dossierUtlnext = Dossier.objects.get(utilsateur = request.user)


        # Cherche la liste de RendezVous de l'utilisateur
        rendez_vous_list = RendezVous.objects.all().filter( dossier__in= dossierUtl)


        context = {
            'dossier': dossierUtl,
            'rendez_vous': rendez_vous_list,
        }

        return render(request, 'profile/rendezvous.html', context = context)

    except:
        context = {
        'dossier': 'error',
        'rendez_vous': False,
        }
        return render(request, 'profile/rendezvous.html', context = context)


@login_required
def view_diagnostic(request, pk):
    #diagnostic = get_object_or_404(Diagnostic,pk=pk)

    #diag = Diagnostic.objects.all().filter( pk = pk)
    #prescription = Prescription.objects.all().filter( diagnostic__in = diag)

    #prescription2 = Prescription.objects.filter( diagnostic = diag)

    #form = DiagnosticForm (instance = diagnostic)

    #context = {
    #'diagnostic': diagnostic,
    #'prescription': prescription,
    #'prescription2': prescription2,
    #}
    #return render(request, 'profile/view_diagnostic.html', context = context )

    diagnostic = get_object_or_404(Diagnostic,pk=pk)
    diag = Diagnostic.objects.all().filter( pk = pk)
    try:
        # Cherche la liste de RendezVous de l'utilisateur
        rendez_vous_list = RendezVous.objects.all().filter( dossier__in= dossierUtl)
        prescription = Prescription.objects.all().filter( diagnostic__in = diag)

        prescription2 = Prescription.objects.all().filter( diagnostic = diag)

        form = DiagnosticForm (instance = diagnostic)

        context = {
        'form': form,
        'diagnostic': diagnostic,
        'prescription': prescription,
        'prescription2': prescription2,
        }

        return render(request, 'profile/view_diagnostic.html', context = context )

    except:
        context = {
        'form': False,
        'diagnostic': diagnostic,
        'prescription': False,
        'prescription2': False,
        }
        return render(request, 'profile/view_diagnostic.html', context = context )
