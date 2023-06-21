# Generated by Django 4.1 on 2022-09-05 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0003_agent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postpackage',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False, verbose_name='Pacakage ID')),
                ('aid', models.IntegerField(verbose_name='Agent ID')),
                ('aname', models.CharField(max_length=25, verbose_name='Agent Name')),
                ('name', models.CharField(max_length=26, verbose_name='Name Of Package')),
                ('area', models.CharField(max_length=25, verbose_name='Preffred Area')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('ptype', models.CharField(max_length=25, verbose_name='Package Type')),
            ],
        ),
    ]