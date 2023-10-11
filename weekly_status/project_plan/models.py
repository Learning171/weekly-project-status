from django.db import models

# Create your models here.
class Account(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    user_choice = (
        ('Admin', 'Admin'),
        ('Project_manager', 'Project_manager'),
        ('Management', 'Management')
    )
    user_type = models.CharField(max_length=20, choices=user_choice)

    def __str__(self):
        return self.user_name


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100, unique=True)
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
    title = models.CharField(max_length=100, unique=True)
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
    report_id = models.ForeignKey(WeeklyReport, on_delete=models.CASCADE, unique=True)
    overall_last_week = models.CharField(max_length=2, choices=color_choice)
    overall_this_week = models.CharField(max_length=2, choices=color_choice)
    scope = models.CharField(max_length=2, choices=color_choice)
    schedule = models.CharField(max_length=2, choices=color_choice)
    cost = models.CharField(max_length=2, choices=color_choice)
    overall_health = models.CharField(max_length=2, choices=color_choice)


class PhaseWiseTimeline(models.Model):
    timeline_id = models.AutoField(primary_key=True)
    report_id = models.ForeignKey(WeeklyReport, on_delete=models.CASCADE)

    
class Phase(models.Model):
     phase_id = models.AutoField(primary_key=True)
     timeline_id = models.ForeignKey(PhaseWiseTimeline, on_delete=models.CASCADE)
     phase_choice = (
          ('Prepare','Prepare'),
          ('Explore','Explore'),
          ('Realize','Realize'),
          ('Deploy','Deploy'),
          ('Run','Run')
     )
     phase_name = models.CharField(max_length=10, choices=phase_choice)
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