# Generated by Django 4.1 on 2022-09-18 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0008_delete_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='status',
            field=models.CharField(default='A', max_length=2, verbose_name='User Status'),
        ),
    ]
