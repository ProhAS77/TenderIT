from datetime import datetime, timedelta

from .models import Task
from django.forms import ModelForm, TextInput, Textarea
from django import forms


#class TaskForm(ModelForm):
 #   class Meta:
  #      model = Task
   #     fields = ['title', 'task', 'user']
    #    widgets = {
     #       'title': TextInput(attrs={
      #          'class': 'form-control',
       #         'placeholder': 'Введите название',
        #    }),
         #   'task': Textarea(attrs={
          #      'class': 'form-control',
           #     'placeholder': 'Введите описание',
           # }),
        #}


class FileForm(forms.Form):
    file = forms.FileField()


class SearchForm(forms.Form):
    ppz_number = forms.IntegerField(label='Номер ППЗ')


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['user', 'category', 'task', 'end_date']
        widgets = {
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }


class TaskUpForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['user', 'category', 'task', 'end_date', 'is_complete']
        widgets = {
            'end_date': forms.DateTimeInput(attrs={'type': 'date'})
        }


