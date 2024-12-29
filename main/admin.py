from django.contrib import admin
from .models import Task, Category

admin.site.register(Task) #Регистрация модели в админке
admin.site.register(Category)