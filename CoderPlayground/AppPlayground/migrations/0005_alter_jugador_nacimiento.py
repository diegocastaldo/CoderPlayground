# Generated by Django 4.1.2 on 2022-11-13 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPlayground', '0004_club_jugador_tarjeta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jugador',
            name='nacimiento',
            field=models.CharField(max_length=30),
        ),
    ]
