from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Project)
admin.site.register(Account)
admin.site.register(WeeklyReport)
admin.site.register(ProjectStatus)
admin.site.register(PhaseWiseTimeline)
admin.site.register(Phase)