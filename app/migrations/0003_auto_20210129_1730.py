# Generated by Django 3.1.5 on 2021-01-29 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210129_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnostic',
            name='chol',
            field=models.IntegerField(default=236, help_text='mg/dl', verbose_name='Serum cholestoral'),
        ),
    ]