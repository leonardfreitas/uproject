# Generated by Django 5.0.4 on 2024-04-25 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='test',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]