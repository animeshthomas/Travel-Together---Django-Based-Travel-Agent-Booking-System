# Generated by Django 4.1.3 on 2022-11-13 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0022_alter_postpackage_aid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postpackage',
            name='aid',
        ),
    ]
