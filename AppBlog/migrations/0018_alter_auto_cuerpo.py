# Generated by Django 4.1 on 2022-10-01 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBlog', '0017_alter_auto_cuerpo_alter_camioneta_cuerpo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='cuerpo',
            field=models.TextField(),
        ),
    ]