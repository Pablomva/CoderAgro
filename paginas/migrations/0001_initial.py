# Generated by Django 4.0.4 on 2022-04-30 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('tema', models.CharField(max_length=250)),
                ('cultivo', models.CharField(max_length=250)),
                ('contenido', models.TextField()),
                ('posteador', models.CharField(max_length=250)),
            ],
        ),
    ]
