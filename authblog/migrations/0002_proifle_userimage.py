# Generated by Django 4.2.2 on 2023-07-03 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proifle',
            name='userimage',
            field=models.ImageField(blank=True, null=True, upload_to='image/profile'),
        ),
    ]
