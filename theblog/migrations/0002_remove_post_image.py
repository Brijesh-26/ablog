# Generated by Django 4.2.2 on 2023-07-01 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]