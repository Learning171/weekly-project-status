# Generated by Django 4.2.5 on 2023-10-05 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
                ('user_email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('user_type', models.CharField(choices=[('Admin', 'Admin'), ('Project_manager', 'Project_manager'), ('Management', 'Management')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=100)),
                ('summary', models.TextField()),
                ('manager_name', models.CharField(max_length=100)),
                ('client_name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_plan.account')),
            ],
        ),
    ]
