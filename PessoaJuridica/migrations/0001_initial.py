# Generated by Django 4.0.5 on 2022-06-23 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=100)),
                ('razaoSocial', models.CharField(max_length=100)),
                ('representanteLegal', models.CharField(max_length=100)),
            ],
        ),
    ]
