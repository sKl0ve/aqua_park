from django.db import models

class Tickets(models.Model):
    name = models.CharField('ФИО', max_length=50)
    number = models.CharField('Номер', max_length=50)
    email = models.CharField('Почта', max_length=50)
    qnt = models.IntegerField('Количество')

    
    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'