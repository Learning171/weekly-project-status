from rest_framework import serializers

from .models import *

class RiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Risk
        fields = '__all__'


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'

class AssumptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assumptions
        fields = '__all__'


class DependencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dependency
        fields = '__all__'
