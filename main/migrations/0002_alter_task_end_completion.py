# Generated by Django 5.1.3 on 2024-12-11 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='end_completion',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='Осталось дней'),
        ),
    ]
