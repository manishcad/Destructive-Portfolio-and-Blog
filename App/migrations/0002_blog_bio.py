# Generated by Django 4.1.5 on 2023-01-11 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='bio',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]