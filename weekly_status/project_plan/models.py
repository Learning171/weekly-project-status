from django.db import models
from account.models import Account

# Create your models here.

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100)
    summary = models.TextField()
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    manager_name = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.project_name
    

class WeeklyReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    week_start_date = models.DateField()
    week_end_date = models.DateField()

    def __str__(self):
        return self.title
    

class ProjectStatus(models.Model):
    color_choice = (
        ('R', 'Red'),
        ('A', 'Amber'),
        ('G', 'Green')
    )
    status_id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    report_id = models.ForeignKey(WeeklyReport, on_delete=models.CASCADE)
    overall_last_week = models.CharField(max_length=6, choices=color_choice)
    overall_this_week = models.CharField(max_length=6, choices=color_choice)
    scope = models.CharField(max_length=6, choices=color_choice)
    schedule = models.CharField(max_length=6, choices=color_choice)
    cost = models.CharField(max_length=6, choices=color_choice)
    overall_health = models.CharField(max_length=6, choices=color_choice)


    def __str__(self):
        return self.status_id


class PhaseWiseTimeline(models.Model):
    timeline_id = models.AutoField(primary_key=True)
    report_id = models.ForeignKey(WeeklyReport, on_delete=models.CASCADE)
    description = models.TextField()
    assignee = models.CharField(max_length=100)


    def __str__(self):
        return self.timeline_id


class TaskToDo(models.Model):
    task_id = models.AutoField(primary_key=True)
    report_id = models.ForeignKey(WeeklyReport, on_delete=models.CASCADE)
    description = models.TextField()
    assignee = models.CharField(max_length=100)


    def __str__(self):
        return self.task_id
    

class Accomplishment(models.Model):
    accomplishment_id = models.AutoField(primary_key=True)
    report_id = models.ForeignKey(WeeklyReport, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
            return self.accomplishment_id


class Assumptions(models.Model):
    assumptions_id = models.AutoField(primary_key=True)
    report_id = models.ForeignKey(WeeklyReport, on_delete=models.CASCADE)
    assumptions = models.TextField()

    def __str__(self):
            return self.assumptions_id
    

class Risk(models.Model):
     risk_id = models.AutoField(primary_key=True)
     report_id = models.ForeignKey(WeeklyReport, on_delete=models.CASCADE)
     severity = models.CharField(max_length=200)
     complexity = models.CharField(max_length=200)
     impact = models.CharField(max_length=200)
     mitigation_plan = models.CharField(max_length=200)
     color_choice = (
        ('R', 'Red'),
        ('A', 'Amber'),
        ('G', 'Green')
    )
     RAGStatus = models.CharField(max_length=6, choices=color_choice)


     def __str__(self):
          return self.risk_id
     

class Issue(models.Model):
     issue_id = models.AutoField(primary_key=True)
     report_id = models.ForeignKey(WeeklyReport, on_delete=models.CASCADE)
     severity = models.CharField(max_length=200)
     complexity = models.CharField(max_length=200)
     impact = models.CharField(max_length=200)
     responsible_party = models.CharField(max_length=200)
     color_choice = (
        ('R', 'Red'),
        ('A', 'Amber'),
        ('G', 'Green')
    )
     RAGStatus = models.CharField(max_length=6, choices=color_choice)


     def __str__(self):
          return self.issue_id
     


class Dependency(models.Model):
     dependency_id = models.AutoField(primary_key=True)
     report_id = models.ForeignKey(WeeklyReport, on_delete=models.CASCADE)
     target_completion_date = models.DateField()
     responsible_party = models.CharField(max_length=200)
     color_choice = (
        ('R', 'Red'),
        ('A', 'Amber'),
        ('G', 'Green')
    )
     RAGStatus = models.CharField(max_length=6, choices=color_choice)


     def __str__(self):
          return self.dependency_id
     

class Phase(models.Model):
     phase_id = models.AutoField(primary_key=True)
     timeline_id = models.ForeignKey(PhaseWiseTimeline, on_delete=models.CASCADE)
     phase_choice = (
          (),
          (),
          (),
          (),
          ()
     )
     Phase_name = models.CharField(max_length=10, choices=phase_choice)
     planned_start_date = models.DateField()
     planned_end_date = models.DateField()
     revised_end_date = models.DateField()
     color_choice = (
        ('R', 'Red'),
        ('A', 'Amber'),
        ('G', 'Green')
    )
     status = models.CharField(max_length=10,choices=color_choice)
     remark = models.TextField()

