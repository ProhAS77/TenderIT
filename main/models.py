from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta, date


class Category(models.Model):
    name = models.CharField('Категория', max_length=50, default='Отсутвует')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Исполнитель')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='Категория')
    author = models.CharField('Автор', max_length=100, default='', null=True, blank=True)
    task = models.TextField('Описание', default='')
    is_complete = models.BooleanField('Завершено', default=False)
    create = models.DateField(auto_now_add=True)
    end_date = models.DateField('Выполнить до')

    def get_days_left(self):
    # метод get_days_left(self) предназначенный для вычисления и отображения количества дней в незавершенных задачах,
    # оставшихся до срока выполнения задачи
        if self.is_complete:
            return ''
        else:
            today = date.today()
            days_left = (self.end_date - today).days
            if days_left < 0:
                return "Просрочка"
            else:
                return days_left

    def __str__(self):
        return self.task

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['is_complete', 'end_date'] #Сортировка по завершению. Упорядочевание набора запроса

