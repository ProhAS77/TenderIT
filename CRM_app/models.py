from django.db import models
import datetime


class Task(models.Model):
    category = models.CharField(max_length=50)
    task_description = models.CharField(max_length=200)
    start_date = models.DateField(default=datetime.date.today())
    deadline = models.DateField()
    executor_name = models.CharField(max_length=100)
    is_overdue = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.deadline is None:
            self.deadline = self.start_date.date() + datetime.timedelta(days=2)
        super(Task, self).save(*args, **kwargs)
