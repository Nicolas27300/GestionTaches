from django.contrib import admin
from lesTaches.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_date', 'due_date')

admin.site.register(Task, TaskAdmin)