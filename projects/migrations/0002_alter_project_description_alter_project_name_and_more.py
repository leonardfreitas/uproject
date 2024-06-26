# Generated by Django 5.0.4 on 2024-04-26 00:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('teams', '0004_alter_team_options_alter_team_created_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='descrição'),
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=50, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='project',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='teams.team', verbose_name='time'),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80, verbose_name='título')),
                ('description', models.TextField(blank=True, null=True, verbose_name='descrição')),
                ('status', models.CharField(choices=[('PENDING', 'Pendente'), ('DONE', 'Finalizado'), ('CANCELED', 'Cancelado')], default='PENDING', max_length=10, verbose_name='status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='data de criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='data de atualização')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project', verbose_name='projeto')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='usuário')),
            ],
            options={
                'verbose_name': 'projeto',
            },
        ),
    ]
