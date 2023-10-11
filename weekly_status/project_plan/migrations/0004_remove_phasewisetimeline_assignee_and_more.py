# Generated by Django 4.2.5 on 2023-10-11 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_plan', '0003_phasewisetimeline_phase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phasewisetimeline',
            name='assignee',
        ),
        migrations.RemoveField(
            model_name='phasewisetimeline',
            name='description',
        ),
        migrations.AlterField(
            model_name='account',
            name='user_email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='projectstatus',
            name='report_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_plan.weeklyreport', unique=True),
        ),
        migrations.AlterField(
            model_name='weeklyreport',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
