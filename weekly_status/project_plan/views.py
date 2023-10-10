from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

# Create your views here.
class RiskView(APIView):
    def get(self, request):
        result = Risk.objects.all()
        riskserializer = RiskSerializer(result, many=True)
        return Response(riskserializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        data = request.data
        riskserializer = RiskSerializer(data=data)
        if riskserializer.is_valid():
            riskserializer.save()
            return Response(riskserializer.data, status=status.HTTP_201_CREATED)
        return Response(riskserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, format=None):
        risk = Risk.objects.get(risk_id=request.data["risk_id"])
        serializer = RiskSerializer(risk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, format=None):
        risk = Risk.objects.get(risk_id=request.data["risk_id"])
        risk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class IssueView(APIView):
    def get(self, request):
        # result = Account.objects.filter(user_id=request.user.user_id)
        result = Issue.objects.all()
        issueserializer = IssueSerializer(result, many=True)
        return Response(issueserializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        data = request.data
        issueserializer = IssueSerializer(data=data)
        if issueserializer.is_valid():
            issueserializer.save()
            return Response(issueserializer.data, status=status.HTTP_201_CREATED)
        return Response(issueserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, format=None):
        issue = Issue.objects.get(issue_id=request.data["issue_id"])
        serializer = IssueSerializer(issue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, format=None):
        issue = Issue.objects.get(issue_id=request.data["issue_id"])
        issue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class AssumptionsView(APIView):
    def get(self, request):
        result = Assumptions.objects.all()
        assumptionsserializer = AssumptionsSerializer(result, many=True)
        return Response(assumptionsserializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        data = request.data
        assumptionsserializer = AssumptionsSerializer(data=data)
        if assumptionsserializer.is_valid():
            assumptionsserializer.save()
            return Response(assumptionsserializer.data, status=status.HTTP_201_CREATED)
        return Response(assumptionsserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, format=None):
        assumptions = Assumptions.objects.get(assumptions_id=request.data["assumptions_id"])
        serializer = AssumptionsSerializer(assumptions, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, format=None):
        assumptions = Assumptions.objects.get(assumptions_id=request.data["assumptions_id"])
        assumptions.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class DependencyView(APIView):
    def get(self, request):
        result = Dependency.objects.all()
        dependencyserializer = DependencySerializer(result, many=True)
        return Response(dependencyserializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        data = request.data
        dependencyserializer = DependencySerializer(data=data)
        if dependencyserializer.is_valid():
            dependencyserializer.save()
            return Response(dependencyserializer.data, status=status.HTTP_201_CREATED)
        return Response(dependencyserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, format=None):
        dependancy = Dependency.objects.get(dependency_id=request.data["dependency_id"])
        serializer = DependencySerializer(dependancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, format=None):
        dependancy = Dependency.objects.get(dependency_id=request.data["dependency_id"])
        dependancy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
