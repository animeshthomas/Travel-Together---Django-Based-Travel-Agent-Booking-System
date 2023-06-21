# Generated by Django 4.1 on 2022-08-23 11:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20, verbose_name='FNAE')),
                ('lname', models.CharField(max_length=20, verbose_name='LNAMW')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Of User')),
                ('uname', models.CharField(max_length=25, verbose_name='Name of User')),
                ('phoneno', models.IntegerField(validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone No')),
                ('state', models.CharField(default='Kerala', max_length=6, verbose_name='State')),
                ('district', models.CharField(choices=[('Alappuzha', 'Alappuzha'), ('Eranakulam', 'Eranakulam'), ('Iduki', 'Iduki'), ('Kannur', 'Kannur'), ('Kasaragod', 'Kasaragod'), ('Kollam', 'Kollam'), ('Kottayam', 'Kottayam'), ('Kozhikode', 'Kozhikode'), ('Malappuram', 'Malappuram'), ('Palakkad', 'Palakkad'), ('Pathanamthiita', 'Pathanamthiita'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Thrissur', 'Thrissur'), ('Wayanad', 'Wayanad')], max_length=20, verbose_name='District')),
                ('address', models.CharField(max_length=250, verbose_name='Address')),
                ('photo', models.ImageField(upload_to='images/', verbose_name='Your Photo')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('password', models.CharField(max_length=25, verbose_name='Password')),
                ('status', models.CharField(default='U', max_length=2, verbose_name='User Status')),
            ],
        ),
    ]