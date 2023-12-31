# Generated by Django 4.2.4 on 2023-08-16 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_employé'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employé',
            name='Nom',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='employé',
            name='Prénom',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='employé',
            name='Salaire_de_Base',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=8),
        ),
    ]
