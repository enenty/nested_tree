from django.db import models


class Tree(models.Model):
    parent = models.ForeignKey('self', models.CASCADE, null=True, verbose_name='Родитель', blank=True)
    name = models.CharField(max_length=255, verbose_name='Название')
