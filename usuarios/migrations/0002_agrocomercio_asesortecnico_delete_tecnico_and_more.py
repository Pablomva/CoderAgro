# Generated by Django 4.0.4 on 2022-04-30 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgroComercio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('razonSocial', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('ubicacion', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('cultivo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='AsesorTecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('provincia', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('cultivo', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Tecnico',
        ),
        migrations.AddField(
            model_name='productor',
            name='cultivo',
            field=models.CharField(default='', max_length=255),
        ),
    ]
