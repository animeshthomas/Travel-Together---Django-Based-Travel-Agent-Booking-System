# Generated by Django 4.1 on 2022-09-05 04:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0002_delete_sample'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('aid', models.IntegerField(primary_key=True, serialize=False, verbose_name='Agent ID')),
                ('aname', models.CharField(max_length=25, verbose_name='Agent Name')),
                ('phoneno', models.IntegerField(validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Phone No')),
                ('state', models.CharField(default='Kerala', max_length=6, verbose_name='State')),
                ('district', models.CharField(choices=[('Alappuzha', 'Alappuzha'), ('Eranakulam', 'Eranakulam'), ('Iduki', 'Iduki'), ('Kannur', 'Kannur'), ('Kasaragod', 'Kasaragod'), ('Kollam', 'Kollam'), ('Kottayam', 'Kottayam'), ('Kozhikode', 'Kozhikode'), ('Malappuram', 'Malappuram'), ('Palakkad', 'Palakkad'), ('Pathanamthiita', 'Pathanamthiita'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('Thrissur', 'Thrissur'), ('Wayanad', 'Wayanad')], max_length=20, verbose_name='District')),
                ('area', models.CharField(max_length=30, verbose_name='Preffred Area')),
                ('address', models.CharField(max_length=250, verbose_name='Address')),
                ('photo', models.ImageField(upload_to='images/', verbose_name='Your Photo')),
                ('verification', models.ImageField(upload_to='images/', verbose_name='Adhar/Election/Driving/PAN ID')),
                ('certification', models.ImageField(upload_to='images/', verbose_name='CTA (Certified Travel Associate) and CTC (Certified Travel Counsellor).')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('password', models.CharField(max_length=25, verbose_name='Password')),
                ('status', models.CharField(default='W', max_length=2, verbose_name='User Status')),
            ],
        ),
    ]
