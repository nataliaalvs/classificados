# Generated by Django 4.1.5 on 2023-01-17 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncios',
            name='celular',
            field=models.IntegerField(),
        ),
    ]
