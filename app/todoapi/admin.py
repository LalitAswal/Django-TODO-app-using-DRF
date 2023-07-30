from django.contrib import admin
from todoapi.models import Task

class TaskAdmin(admin.ModelAdmin):
    pass

admin.site.register(Task, TaskAdmin)
