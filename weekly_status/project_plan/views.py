from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

# Create your views here.
class ProjectView(APIView):
    def get(self, request):
        # result = Project.objects.filter(user_id=request.user.user_id)
        result = Project.objects.all()
        projectserializer = ProjectSerializer(result, many=True)
        return Response(projectserializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        data = request.data
        projectserializer = ProjectSerializer(data=data)
        if projectserializer.is_valid():
            projectserializer.save()
            return Response(projectserializer.data, status=status.HTTP_201_CREATED)
        return Response(projectserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, format=None):
        project = Project.objects.get(project_id=request.data["project_id"])
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, format=None):
        project = Project.objects.get(project_id=request.data["project_id"])
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class AccountView(APIView):
    def get(self, request):
        # result = Account.objects.filter(user_id=request.user.user_id)
        result = Account.objects.all()
        accountserializer = AccountSerializer(result, many=True)
        return Response(accountserializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        data = request.data
        accountserializer = AccountSerializer(data=data)
        if accountserializer.is_valid():
            accountserializer.save()
            return Response(accountserializer.data, status=status.HTTP_201_CREATED)
        return Response(accountserializer.errors, status=status.HTTP_400_BAD_REQUEST)
