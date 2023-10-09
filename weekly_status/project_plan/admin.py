from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(WeeklyReport)
admin.site.register(Project)
admin.site.register(ProjectStatus)
admin.site.register(PhaseWiseTimeline)
admin.site.register(TaskToDo)
admin.site.register(Accomplishment)
admin.site.register(Assumptions)
admin.site.register(Risk)
admin.site.register(Issue)
admin.site.register(Dependency)
