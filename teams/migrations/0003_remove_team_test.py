# Generated by Django 5.0.4 on 2024-04-25 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_team_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='test',
        ),
    ]
