from django.db import models

# Create your models here.
class Account(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100)
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
    overall_last_week = models.CharField(max_length=2, choices=color_choice)
    overall_this_week = models.CharField(max_length=2, choices=color_choice)
    scope = models.CharField(max_length=2, choices=color_choice)
    schedule = models.CharField(max_length=2, choices=color_choice)
    cost = models.CharField(max_length=2, choices=color_choice)
    overall_health = models.CharField(max_length=2, choices=color_choice)


    def __str__(self):
        return self.status_id