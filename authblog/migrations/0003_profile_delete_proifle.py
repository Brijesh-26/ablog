# Generated by Django 4.2.2 on 2023-07-04 06:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import localflavor.in_.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authblog', '0002_proifle_userimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.IntegerField()),
                ('userimage', models.ImageField(blank=True, null=True, upload_to='image/profile')),
                ('address', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('state', localflavor.in_.models.INStateField(max_length=2)),
                ('bio', models.TextField(max_length=1000)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Proifle',
        ),
    ]
