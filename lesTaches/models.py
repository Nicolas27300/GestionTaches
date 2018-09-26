from django.db import models
from datetime import date, timedelta
from django.template.defaultfilters import date as django_date
from django.utils.html import format_html

class Task(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    scheduled_date = models.DateField(null=True)
    due_date = models.DateField(null=True)
    closed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def colored_due_date(self):
        due_date = django_date(self.due_date, "d F Y")
        if self.due_date-timedelta(days=7) > date.today():
            color="green"
        elif self.due_date > date.today():
            color="orange"
        else:
            color="red"
        return format_html("<span style=color:%s>%s</span>" % (color, due_date))
    
    #colored_due_date.allow_tag


