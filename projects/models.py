from django.db import models
from django.contrib.auth import get_user_model

from teams.models import Team


User = get_user_model()


class Project(models.Model):
    name = models.CharField('nome', max_length=50)
    description = models.TextField('descrição', null=True, blank=True)
    team = models.ForeignKey(Team, verbose_name='time', on_delete=models.PROTECT)
    created_at = models.DateTimeField('data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'projeto'
    
    def __str__(self):
        return self.name



class Task(models.Model):

    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pendente'
        DONE = 'DONE', 'Finalizado'
        CANCELED = 'CANCELED', 'Cancelado'

    title = models.CharField('título', max_length=80)
    description = models.TextField('descrição', null=True, blank=True)
    status = models.CharField('status', max_length=10, 
                              choices=Status.choices, default=Status.PENDING)
    user = models.ForeignKey(User, null=True, blank=True, 
                             verbose_name='usuário', on_delete=models.SET_NULL)
    project = models.ForeignKey(Project, verbose_name='projeto', on_delete=models.CASCADE)
    created_at = models.DateTimeField('data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'tarefa'
    
    def __str__(self):
        return self.title