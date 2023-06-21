# Generated by Django 4.1 on 2022-10-04 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0013_delete_postpackage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postpackage',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False, verbose_name='Pacakage ID')),
                ('aid', models.IntegerField(verbose_name='Agent ID')),
                ('aname', models.CharField(max_length=26, verbose_name='Name Of Agent')),
                ('name', models.CharField(max_length=26, verbose_name='Name Of Package')),
                ('area', models.CharField(max_length=25, verbose_name='Preffred Area')),
                ('description', models.CharField(max_length=100, verbose_name='Description')),
                ('ptype', models.CharField(max_length=25, verbose_name='Package Type')),
                ('photo1', models.ImageField(upload_to='images/', verbose_name='Photo')),
                ('photo2', models.ImageField(default='none', upload_to='images/', verbose_name='Your Photo')),
                ('photo3', models.ImageField(upload_to='images/', verbose_name='Your Photo')),
                ('photo4', models.ImageField(upload_to='images/', verbose_name='Your Photo')),
            ],
        ),
    ]