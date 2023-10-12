from django.db import models

# Create your models here.
class WeeklyReport(models.Model):
    ReportID = models.IntegerField(auto_created=True,primary_key=True)
    Title = models.CharField(max_length=50)
    WeekStartDate = models.DateField(auto_now_add=True)
    WeekEndDate = models.DateField(auto_now_add=True)

    def __str__(self) :
        return self.ReportID

class TaskToDo(models.Model):
    TaskID = models.IntegerField()
    ReportID = models.ForeignKey(WeeklyReport,on_delete=models.CASCADE,null=False)
    Description = models.TextField()
    Assignee = models.CharField(max_length=50)


class Accomplishment(models.Model):
    AccomplishmentID = models.IntegerField()
    ReportID = models.ForeignKey(WeeklyReport,on_delete=models.CASCADE,null=False)
    Description = models.TextField()
