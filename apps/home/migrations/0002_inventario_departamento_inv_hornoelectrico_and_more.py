# Generated by Django 4.1 on 2022-09-06 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventario_departamento',
            name='INV_HORNOELECTRICO',
            field=models.BooleanField(default=False, verbose_name='Microondas'),
        ),
        migrations.AddField(
            model_name='inventario_departamento',
            name='INV_MICROONDAS',
            field=models.BooleanField(default=False, verbose_name='Microondas'),
        ),
    ]
