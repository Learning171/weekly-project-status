from django.db import models

# Create your models here.
class Account(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    user_choice = (
        ('Admin', 'Admin'),
        ('Project_manager', 'Project Manager'),
        ('Management', 'Management')
    )
    user_type = models.CharField(max_length=20, choices=user_choice)

    def __str__(self):
        return self.user_name