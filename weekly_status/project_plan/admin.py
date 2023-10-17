from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Project)
admin.site.register(WeeklyReport)
admin.site.register(ProjectStatus)
admin.site.register(PhaseWiseTimeline)
admin.site.register(Phase)
admin.site.register(TaskToDo)
admin.site.register(Accomplishment)
admin.site.register(Assumption)
admin.site.register(Risk)
admin.site.register(Issue)
admin.site.register(Dependency)
