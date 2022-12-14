# Generated by Django 4.1.2 on 2022-11-06 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPlayground', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cajonera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('medida', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('cajones', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Escritorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('medida', models.IntegerField()),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mesaluz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('medida', models.IntegerField()),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='nobel',
        ),
    ]
