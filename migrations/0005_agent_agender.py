# Generated by Django 4.1 on 2022-09-13 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0004_postpackage'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='agender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1, verbose_name='Gender'),
        ),
    ]
