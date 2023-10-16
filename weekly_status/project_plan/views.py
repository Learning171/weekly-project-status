from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *
from .utils import *


class ProjectView(AllViewsMixin, APIView):
    model = Project
    serializer = ProjectSerializer


    def put(self, request, format=None):
        project = Project.objects.get(project_id=request.data["project_id"])
        projectserializer = ProjectSerializer(project, data=request.data)
        if projectserializer.is_valid():
            projectserializer.save()
            return Response(projectserializer.data, status=status.HTTP_200_OK)
        return Response(projectserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, format=None):
        project = Project.objects.get(project_id=request.data["project_id"])
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class AccountView(AllViewsMixin, APIView):
    model = Account
    serializer = AccountSerializer



class WeeklyReportView(AllViewsMixin, APIView):
    model = WeeklyReport
    serializer = WeeklyReportSerializer

    # def get(self, request):
    #     result = WeeklyReport.objects.all()
    #     weeklyreportserializer = WeeklyReportSerializer(result, many=True)
    #     return Response(weeklyreportserializer.data, status=status.HTTP_200_OK)
    

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
    


class ProjectStatusView(AllViewsMixin, APIView):
    model = ProjectStatus
    serializer = ProjectStatusSerializer

    # def get(self, request):
    #     result = ProjectStatus.objects.all()
    #     projectstatusserializer = ProjectStatusSerializer(result, many=True)
    #     return Response(projectstatusserializer.data, status=status.HTTP_200_OK)
    

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
    


class PhaseWiseTimelineView(AllViewsMixin, APIView):
    model = PhaseWiseTimeline
    serializer = PhaseWiseTimelineSerializer

    # def get(self, request):
    #     result = PhaseWiseTimeline.objects.all()
    #     phasewisetimelineserializer = PhaseWiseTimelineSerializer(result, many=True)
    #     return Response(phasewisetimelineserializer.data, status=status.HTTP_200_OK)
    
    
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
    


class PhaseView(AllViewsMixin, APIView):
    model = Phase
    serializer = PhaseSerializer

    # def get(self, request):
    #     result = Phase.objects.all()
    #     phaseserializer = PhaseSerializer(result, many=True)
    #     return Response(phaseserializer.data, status=status.HTTP_200_OK)
    
    
    def put(self, request, format=None):
        phase = Phase.objects.filter(timeline_id=request.data[0]["timeline_id"])
        phaseserializer = PhaseSerializer(phase, data=request.data)
        if phaseserializer.is_valid():
            phaseserializer.save()
            return Response(phaseserializer.data)
        return Response(phaseserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, format=None):
        phase = Phase.objects.filter(timeline_id=request.data["timeline_id"])
        phase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class TaskToDoView(AllViewsMixin, APIView):
    model = TaskToDo
    serializer = TaskToDoSerializers

    # def get(self,request):
    #     result = TaskToDo.objects.all()
    #     serializers = TaskToDoSerializers(result,many = True)
    #     return Response(serializers.data)

    
    def patch(self, request):
        result = TaskToDo.objects.get(TaskID=request.data["TaskID"])
        serializer = TaskToDoSerializers(result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
             

    def delete(self, request):
        try:
            result =TaskToDo.objects.filter(TaskID=request.data["TaskID"])
            result.delete()
            return Response({"status": "success", "message": "Record Deleted"})
        except Exception as e:
            return Response({"status": "error", "meassage": e})
        
 
        
class AccomplishmentView(AllViewsMixin, APIView):
    model = Accomplishment
    serializer = AccomplishmentSerializers

    # def get(self,request):
    #     result = Accomplishment.objects.all()
    #     serializers = AccomplishmentSerializers(result,many = True)
    #     return Response(serializers.data)

    
    def patch(self,request):
        result = Accomplishment.objects.get(AccomplishmentID=request.data["AccomplishmentID"])
        serializer = AccomplishmentSerializers(result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
        
    def delete(self, request):
        try:
            result =Accomplishment.objects.filter(AccomplishmentID=request.data["AccomplishmentID"])
            result.delete()
            return Response({"status": "success", "message": "Record Deleted"})
        except Exception as e:
            return Response({"status": "error", "meassage": e})
        

class RiskView(APIView):
    # def get(self, request):
    #     result = Risk.objects.all()
    #     riskserializer = RiskSerializer(result, many=True)
    #     return Response(riskserializer.data, status=status.HTTP_200_OK)
    

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
    # def get(self, request):
    #     # result = Account.objects.filter(user_id=request.user.user_id)
    #     result = Issue.objects.all()
    #     issueserializer = IssueSerializer(result, many=True)
    #     return Response(issueserializer.data, status=status.HTTP_200_OK)
    
    
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
    


class AssumptionView(APIView):
    # def get(self, request):
    #     result = Assumption.objects.all()
    #     assumptionsserializer = AssumptionSerializer(result, many=True)
    #     return Response(assumptionsserializer.data, status=status.HTTP_200_OK)
    

    def put(self, request, format=None):
        assumption = Assumption.objects.get(assumption_id=request.data["assumption_id"])
        serializer = AssumptionSerializer(assumption, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, format=None):
        assumption = Assumption.objects.get(assumption_id=request.data["assumption_id"])
        assumption.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class DependencyView(APIView):
    # def get(self, request):
    #     result = Dependency.objects.all()
    #     dependencyserializer = DependencySerializer(result, many=True)
    #     return Response(dependencyserializer.data, status=status.HTTP_200_OK)
    
    
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