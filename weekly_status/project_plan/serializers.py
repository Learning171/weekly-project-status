from rest_framework import serializers
from .models import WeeklyReport,TaskToDo,Accomplishment

class WeeklyReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = WeeklyReport
        fields = ['ReportID','Title',"WeekStartDate",'WeekEndDate']


class TaskToDoSerializers(serializers.ModelSerializer):
    class Meta:
        model =TaskToDo
        fields = ["TaskID","ReportID","Description","Assignee"]

class AccomplishmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Accomplishment
        fields = ["AccomplishmentID","ReportID","Description"]