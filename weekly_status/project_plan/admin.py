from django.contrib import admin
from .models import TaskToDo,WeeklyReport,Accomplishment
# Register your models here.
admin.site.register(WeeklyReport)
class WeeklyReportAdmin(admin.ModelAdmin):
    list_display = ['ReportID', 'Title', 'WeekStartDate', 'WeekEndDate']


admin.site.register(TaskToDo)
class TaskToDoAdmin(admin.ModelAdmin):
    list_display = ['TaskID', 'ReportID', 'Description', 'Assignee']


admin.site.register(Accomplishment)
class AccomplishmentAdmin(admin.ModelAdmin):
    list_display = ['AccomplishmentID', 'ReportID', 'Description']