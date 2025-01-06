from .models import Task
from django.forms import ModelForm
from django import forms


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


