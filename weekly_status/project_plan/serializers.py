from django.db.models import fields

from rest_framework import serializers

from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class ProjectStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStatus
        fields = '__all__'


class WeeklyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyReport
        fields = '__all__'


class PhaseWiseTimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhaseWiseTimeline
        fields = '__all__'


class PhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phase
        fields = '__all__'


class TaskToDoSerializers(serializers.ModelSerializer):
    class Meta:
        model =TaskToDo
        fields = '__all__'


class AccomplishmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Accomplishment
        fields = '__all__'


class RiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Risk
        fields = '__all__'


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'

class AssumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assumption
        fields = '__all__'


class DependencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependency
        fields = '__all__'
