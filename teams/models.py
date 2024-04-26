from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class Team(models.Model):
    name = models.CharField('nome', max_length=30)
    users = models.ManyToManyField(User, verbose_name='usuários')
    created_at = models.DateTimeField('data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'time'
        verbose_name_plural = 'times'

    def __str__(self):
        return self.name
