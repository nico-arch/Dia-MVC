# Generated by Django 3.1.4 on 2021-01-28 21:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210127_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnostic',
            name='cp',
            field=models.CharField(blank=True, choices=[('0', 'Valeur: 0'), ('1', 'Valeur: 1'), ('2', 'Valeur: 2'), ('3', 'Valeur: 3')], default='0', help_text='(4 values)', max_length=1, verbose_name='Chest pain type'),
        ),
        migrations.AddField(
            model_name='dossier',
            name='dateDeNaissance',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Date de naissance'),
        ),
        migrations.AddField(
            model_name='dossier',
            name='sex',
            field=models.CharField(blank=True, choices=[('0', 'M'), ('1', 'F')], default='0', max_length=1, verbose_name='Sexe'),
        ),
        migrations.AlterField(
            model_name='dossier',
            name='identifiantCin_Nif',
            field=models.CharField(max_length=200, null=True, verbose_name='Cin ou Nif'),
        ),
    ]