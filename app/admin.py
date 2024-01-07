from django.contrib import admin

from app.models import Task
class TaskAdmin(admin.ModelAdmin):
    list_display=('task','updated_at','created_at','is_completed')
    search_fields=('task',)
admin.site.register(Task,TaskAdmin)
