# Generated by Django 4.1 on 2022-09-17 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0002_alter_auto_imagen_alter_camioneta_imagen_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auto',
            name='imagen',
        ),
        migrations.CreateModel(
            name='AutoImagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(null=True, upload_to='autos')),
                ('vehiculo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AppBlog.auto')),
            ],
        ),
    ]