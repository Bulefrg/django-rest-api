# Generated by Django 3.1.8 on 2024-04-05 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['-id']},
        ),
    ]
