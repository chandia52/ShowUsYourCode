# Generated by Django 4.2.6 on 2024-01-24 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_proyecto_delete_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/proyectos/'),
        ),
    ]
