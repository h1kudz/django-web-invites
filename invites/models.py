from django.db import models
from django.urls import reverse

class Invites(models.Model):
    name = models.CharField(max_length=150, verbose_name= 'ФИО')
    comment = models.TextField(blank=True, verbose_name='Коммент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Редактировано')
    is_confirm = models.BooleanField(default=False, verbose_name='Подтверждения!')
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('view_invites', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Web-приглосительное'
        verbose_name_plural = 'Пригласительные'
        ordering = ['-created_at']