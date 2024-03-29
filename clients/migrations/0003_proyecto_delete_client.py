# Generated by Django 4.2.6 on 2024-01-22 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_client_bio_client_img_alter_client_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='images/projectos')),
            ],
        ),
        migrations.DeleteModel(
            name='Client',
        ),
    ]
