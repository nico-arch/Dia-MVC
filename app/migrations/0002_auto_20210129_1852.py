# Generated by Django 3.1.4 on 2021-01-29 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnostic',
            name='cp',
            field=models.CharField(choices=[('0', 'Valeur: 0'), ('1', 'Valeur: 1'), ('2', 'Valeur: 2'), ('3', 'Valeur: 3')], default='1', help_text='(4 values)', max_length=13, verbose_name='Chest pain type'),
        ),
    ]