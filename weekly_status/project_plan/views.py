from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

from .models import *
from .serializers import *


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
        projectserializer = ProjectSerializer(project, data=request.data)
        if projectserializer.is_valid():
            projectserializer.save()
            return Response(projectserializer.data)
        return Response(projectserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

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



class WeeklyReportView(APIView):
    def get(self, request):
        result = WeeklyReport.objects.all()
        weeklyreportserializer = WeeklyReportSerializer(result, many=True)
        return Response(weeklyreportserializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        data = request.data
        weeklyreportserializer = WeeklyReportSerializer(data=data)
        if weeklyreportserializer.is_valid():
            weeklyreportserializer.save()
            return Response(weeklyreportserializer.data, status=status.HTTP_201_CREATED)
        return Response(weeklyreportserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, format=None):
        weeklyreport = WeeklyReport.objects.get(project_id=request.data["project_id"], report_id=request.data["report_id"])
        weeklyreportserializer = WeeklyReportSerializer(weeklyreport, data=request.data)
        if weeklyreportserializer.is_valid():
            weeklyreportserializer.save()
            return Response(weeklyreportserializer.data)
        return Response(weeklyreportserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, format=None):
        weeklyreport = WeeklyReport.objects.get(project_id=request.data["project_id"], report_id=request.data["report_id"])
        weeklyreport.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class ProjectStatusView(APIView):
    def get(self, request):
        result = ProjectStatus.objects.all()
        projectstatusserializer = ProjectStatusSerializer(result, many=True)
        return Response(projectstatusserializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
        data = request.data
        projectstatusserializer = ProjectStatusSerializer(data=data)
        if projectstatusserializer.is_valid():
            projectstatusserializer.save()
            return Response(projectstatusserializer.data, status=status.HTTP_201_CREATED)
        return Response(projectstatusserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def put(self, request, format=None):
        projectstatus = ProjectStatus.objects.get(project_id=request.data["project_id"], 
                                                  report_id=request.data["report_id"], 
                                                  status_id=request.data["status_id"])
        projectstatusserializer = ProjectStatusSerializer(projectstatus, data=request.data)
        if projectstatusserializer.is_valid():
            projectstatusserializer.save()
            return Response(projectstatusserializer.data)
        return Response(projectstatusserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, format=None):
        projectstatus = ProjectStatus.objects.get(project_id=request.data["project_id"], 
                                                  report_id=request.data["report_id"], 
                                                  status_id=request.data["status_id"])
        projectstatus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class PhaseWiseTimelineView(APIView):
    def get(self, request):
        result = PhaseWiseTimeline.objects.filter(timeline_id = 1)
        phasewisetimelineserializer = PhaseWiseTimelineSerializer(result, many=True)
        return Response(phasewisetimelineserializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        phaseWisetimelineserializer = PhaseWiseTimelineSerializer(data=data)
        if phaseWisetimelineserializer.is_valid():
            phaseWisetimelineserializer.save()
            return Response(phaseWisetimelineserializer.data, status=status.HTTP_201_CREATED)
        return Response(phaseWisetimelineserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def put(self, request, format=None):
    #     phasewisetimeline = PhaseWiseTimeline.objects.get(timeline_id = 1)
    #     phasewisetimelineserializer = PhaseWiseTimelineSerializer(phasewisetimeline, data=request.data)
    #     if phasewisetimelineserializer.is_valid():
    #         phasewisetimelineserializer.save()
    #         return Response(phasewisetimelineserializer.data)
    #     return Response(phasewisetimelineserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    # def delete(self, request, format=None):
    #     phasewisetimeline = PhaseWiseTimeline.objects.get(timeline_id = 1)
    #     phasewisetimeline.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    


class PhaseView(APIView):
    def get(self, request):
        result = Phase.objects.all()
        phaseserializer = PhaseSerializer(result, many=True)
        return Response(phaseserializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        phaseserializer = PhaseSerializer(data=data, many=True)
        if phaseserializer.is_valid():
            phaseserializer.save()
            return Response(phaseserializer.data, status=status.HTTP_201_CREATED)
        return Response(phaseserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, format=None):
        phase = Phase.objects.get(timeline_id = 1)
        phaseserializer = PhaseSerializer(phase, data=request.data)
        if phaseserializer.is_valid():
            phaseserializer.save()
            return Response(phaseserializer.data)
        return Response(phaseserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, format=None):
        phase = Phase.objects.get(timeline_id = 1)
        phase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)