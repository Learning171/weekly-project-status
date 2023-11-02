from django.db import models

from account.models import *

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=100, unique=True)
    summary = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manager_name = models.CharField(max_length=100, blank=True)
    client_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def save(self, *args, **kwargs):
        self.manager_name = self.user.user_name
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.project_name
    

class WeeklyReport(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True, blank=True)
    week_start_date = models.DateField()
    week_end_date = models.DateField()

    def save(self, *args, **kwargs):
        self.title = f"{self.week_end_date} - {self.project.project_name}"
        super(WeeklyReport, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectStatus(models.Model):
    color_choice = (
        ('R', 'Red'),
        ('A', 'Amber'),
        ('G', 'Green')
    )
    report = models.OneToOneField(WeeklyReport, on_delete=models.CASCADE)
    overall_last_week = models.CharField(max_length=2, choices=color_choice)
    overall_this_week = models.CharField(max_length=2, choices=color_choice)
    scope = models.CharField(max_length=2, choices=color_choice)
    schedule = models.CharField(max_length=2, choices=color_choice)
    cost = models.CharField(max_length=2, choices=color_choice)
    overall_health = models.CharField(max_length=2, choices=color_choice)


class PhaseWiseTimeline(models.Model):
    report = models.OneToOneField(WeeklyReport, on_delete=models.CASCADE)
    timeline_title = models.CharField(max_length=200)

    
class Phase(models.Model):
    timeline = models.ForeignKey(PhaseWiseTimeline, on_delete=models.CASCADE)
    # phase_choice = (
    #     ('Prepare','Prepare'),
    #     ('Explore','Explore'),
    #     ('Realize','Realize'),
    #     ('Deploy','Deploy'),
    #     ('Run','Run')
    # )
    # phase_name = models.CharField(max_length=10, choices=phase_choice)
    phase_name = models.CharField(max_length=20)
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


class TaskToDo(models.Model):
    report = models.ForeignKey(WeeklyReport,on_delete=models.CASCADE,null=False)
    description = models.TextField()
    assignee = models.CharField(max_length=50)


class Accomplishment(models.Model):
    report = models.ForeignKey(WeeklyReport,on_delete=models.CASCADE,null=False)
    Description = models.TextField()


class Assumption(models.Model):
    report = models.ForeignKey(WeeklyReport, on_delete=models.CASCADE)
    assumption = models.TextField()

    def __str__(self):
            return self.assumption
    

class Risk(models.Model):
    report = models.ForeignKey(WeeklyReport, on_delete=models.CASCADE)
    risk_description = models.TextField()
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
        return self.risk_description
     

class Issue(models.Model):
    report = models.ForeignKey(WeeklyReport, on_delete=models.CASCADE)
    issue_description = models.TextField()
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
        return self.issue_description
     


class Dependency(models.Model):
    report = models.ForeignKey(WeeklyReport, on_delete=models.CASCADE)
    dependency_description = models.CharField(max_length=200)
    target_completion_date = models.DateField()
    responsible_party = models.CharField(max_length=200)
    color_choice = (
        ('R', 'Red'),
        ('A', 'Amber'),
        ('G', 'Green')
    )
    RAGStatus = models.CharField(max_length=6, choices=color_choice)


    def __str__(self):
        return self.dependency_description