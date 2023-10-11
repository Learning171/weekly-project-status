# Generated by Django 4.2.5 on 2023-10-05 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_plan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyReport',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('week_start_date', models.DateField()),
                ('week_end_date', models.DateField()),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_plan.project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectStatus',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('overall_last_week', models.CharField(choices=[('R', 'Red'), ('A', 'Amber'), ('G', 'Green')], max_length=2)),
                ('overall_this_week', models.CharField(choices=[('R', 'Red'), ('A', 'Amber'), ('G', 'Green')], max_length=2)),
                ('scope', models.CharField(choices=[('R', 'Red'), ('A', 'Amber'), ('G', 'Green')], max_length=2)),
                ('schedule', models.CharField(choices=[('R', 'Red'), ('A', 'Amber'), ('G', 'Green')], max_length=2)),
                ('cost', models.CharField(choices=[('R', 'Red'), ('A', 'Amber'), ('G', 'Green')], max_length=2)),
                ('overall_health', models.CharField(choices=[('R', 'Red'), ('A', 'Amber'), ('G', 'Green')], max_length=2)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_plan.project')),
                ('report_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_plan.weeklyreport')),
            ],
        ),
    ]