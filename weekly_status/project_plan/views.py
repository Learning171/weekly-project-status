from django.shortcuts import render
from django.shortcuts import get_list_or_404
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *


class AllPostsMixin:
    model = None
    serializer = None

    def post(self, request):
        try:
            data = request.data
            serializer = self.serializer(data=data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_201_CREATED)
            return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)


class ProjectView(AllPostsMixin, APIView):
    model = Project
    serializer = ProjectSerializer

    def get(self, request):
        try:
            result = Project.objects.filter(user_id=request.user.id)
            projectserializer = ProjectSerializer(result, many=True)
            return Response(projectserializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
        
    
    def put(self, request, format=None):
        try:
            project = Project.objects.get(
                user_id=request.user.id,
                id=request.data["project_id"]
            )
            projectserializer = ProjectSerializer(project, data=request.data)
            if projectserializer.is_valid():
                projectserializer.save()
                return Response(projectserializer.data, status=status.HTTP_200_OK)
            return Response(projectserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    

    def delete(self, request, pk, format=None):
        try:
            project = Project.objects.get(
                user_id=request.user.id,
                id=pk
            )
            project.delete()
            return Response({"status": "success", "message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)


class ProjectDetailView(APIView):
    def get(self, request, pk):
        try:
            result = Project.objects.get(
                user_id=request.user.id,
                id=pk
            )
            serializer = ProjectSerializer(result)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    

class ProjectWeeklyReportView(AllPostsMixin, APIView):
    model = WeeklyReport
    serializer = WeeklyReportSerializer

    def get(self, request, pk):
        try:
            result = WeeklyReport.objects.filter(
                project_id=pk
            )
            weeklyreportserializer = WeeklyReportSerializer(result, many=True)
            return Response(weeklyreportserializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
        

    def put(self, request, format=None):
        try:
            weeklyreport = WeeklyReport.objects.get(
                project_id=request.data["project"],
                id=request.data["report_id"]
            )
            weeklyreportserializer = WeeklyReportSerializer(weeklyreport, data=request.data)
            if weeklyreportserializer.is_valid():
                weeklyreportserializer.save()
                return Response(weeklyreportserializer.data)
            return Response(weeklyreportserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    

    def delete(self, request, pk, format=None):
        try:
            weeklyreport = WeeklyReport.objects.get(
                id=pk
            )
            weeklyreport.delete()
            return Response({"status": "success", "message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    

class AllWeeklyReportView(APIView):
    def get(self, request):
        try:
            user_projects = Project.objects.filter(user_id=request.user.id)
            user_projects_ids = [project.id for project in user_projects]
            result = WeeklyReport.objects.filter(project_id__in=user_projects_ids)
            weeklyreportserializer = WeeklyReportSerializer(result, many=True)
            return Response(weeklyreportserializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)


class ProjectStatusView(AllPostsMixin, APIView):
    model = ProjectStatus
    serializer = ProjectStatusSerializer

    def get(self, request, pk):
        try:
            result = ProjectStatus.objects.filter(
                report_id=pk
            )
            projectstatusserializer = ProjectStatusSerializer(result, many=True)
            return Response(projectstatusserializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
        
    
    def put(self, request, format=None):
        try:
            projectstatus = ProjectStatus.objects.get(
                report_id=request.data["report"],
                id=request.data["status_id"]
            )
            projectstatusserializer = ProjectStatusSerializer(projectstatus, data=request.data)
            if projectstatusserializer.is_valid():
                projectstatusserializer.save()
                return Response(projectstatusserializer.data)
            return Response(projectstatusserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    

    def delete(self, request, pk, format=None):
        try:
            projectstatus = ProjectStatus.objects.get(
                id=pk
            )
            projectstatus.delete()
            return Response({"status": "success", "message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    


class PhaseWiseTimelineView(AllPostsMixin, APIView):
    model = PhaseWiseTimeline
    serializer = PhaseWiseTimelineSerializer

    def get(self, request, pk):
        try:
            result = PhaseWiseTimeline.objects.filter(
                id=pk
            )
            phasewisetimelineserializer = PhaseWiseTimelineSerializer(result, many=True)
            return Response(phasewisetimelineserializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
        

    def put(self, request, format=None):
        try:
            phasewisetimeline = PhaseWiseTimeline.objects.get(
                user_id=request.user.id,
                project_id=request.data["project_id"],
                report_id=request.data["report_id"]
            )
            phasewisetimelineserializer = PhaseWiseTimelineSerializer(phasewisetimeline, data=request.data)
            if phasewisetimelineserializer.is_valid():
                phasewisetimelineserializer.save()
                return Response(phasewisetimelineserializer.data)
            return Response(phasewisetimelineserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    

    def delete(self, request, pk, format=None):
        try:
            phasewisetimeline = PhaseWiseTimeline.objects.get(
                id=pk
            )
            phasewisetimeline.delete()
            return Response({"status": "success", "message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    


class PhaseView(AllPostsMixin, APIView):
    model = Phase
    serializer = PhaseSerializer

    def get(self, request, pk):
        try:
            result = Phase.objects.filter(
                timeline_id=pk
            )
            phaseserializer = PhaseSerializer(result, many=True)
            return Response(phaseserializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
        

    def put(self, request, format=None):
        try:
            phase = Phase.objects.get(
                user_id=request.user.id,
                project_id=request.data["project_id"],
                report_id=request.data["report_id"],
                timeline_id=request.data["timeline_id"],
                phase_name=request.data["phase_name"]
            )
            phaseserializer = PhaseSerializer(phase, data=request.data)
            if phaseserializer.is_valid():
                phaseserializer.save()
                return Response(phaseserializer.data)
            return Response(phaseserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    

    def delete(self, request, pk, format=None):
        try:
            phase = Phase.objects.filter(
                timeline_id=pk
            )
            phase.delete()
            return Response({"status": "success", "message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    


class TaskToDoView(AllPostsMixin, APIView):
    model = TaskToDo
    serializer = TaskToDoSerializer

    def get(self, request, pk):
        try:
            result = TaskToDo.objects.filter(
                report_id=pk
            )
            tasktodoserializer = TaskToDoSerializer(result, many = True)
            return Response(tasktodoserializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
        

    def patch(self, request):
        try:
            result = TaskToDo.objects.get(
                user_id=request.user.id,
                project_id=request.data["project_id"],
                report_id=request.data["report_id"],
                id=request.data["tasktodo_id"]
            )
            tasktodoserializer = TaskToDoSerializer(result, data=request.data, partial=True)
            if tasktodoserializer.is_valid():
                tasktodoserializer.save()
                return Response({"status": "success", "data": tasktodoserializer.data})
            return Response({"status": "error", "data": tasktodoserializer.errors})
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
             

    def delete(self, request, pk):
        try:
            result =TaskToDo.objects.get(
                id=pk
            )
            result.delete()
            return Response({"status": "success", "message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"status": "error", "meassage": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
        
 
        
class AccomplishmentView(AllPostsMixin, APIView):
    model = Accomplishment
    serializer = AccomplishmentSerializer

    def get(self, request, pk):
        try:
            result = Accomplishment.objects.filter(
                report_id=pk
            )
            accomplishmentserializers = AccomplishmentSerializer(result,many = True)
            return Response(serializers.data)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
        

    def patch(self,request):
        try:
            result = Accomplishment.objects.get(
                user_id=request.user.id,
                project_id=request.data["project_id"],
                report_id=request.data["report_id"],
                accomplishment_id=request.data["accomplishment_id"]
            )
            accomplishmentserializers = AccomplishmentSerializer(result, data=request.data, partial=True)
            if accomplishmentserializers.is_valid():
                accomplishmentserializers.save()
                return Response({"status": "success", "data": accomplishmentserializers.data})
            return Response({"status": "error", "data": accomplishmentserializers.errors})
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request, pk):
        try:
            result =Accomplishment.objects.get(
                id=pk
            )
            result.delete()
            return Response({"status": "success", "message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"status": "error", "meassage": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
        

class RiskView(AllPostsMixin, APIView):
    model = Risk
    serializer = RiskSerializer
    
    def get(self, request, pk):
        try:
            result = Risk.objects.filter(
                report_id=pk
            )
            riskserializer = RiskSerializer(result,many = True)
            return Response(riskserializer.data)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
        

    def put(self, request, format=None):
        try:
            risk = Risk.objects.get(
                user_id=request.user.id,
                project_id=request.data["project_id"],
                report_id=request.data["report_id"],
                risk_id=request.data["risk_id"]
            )
            riskserializer = RiskSerializer(risk, data=request.data)
            if riskserializer.is_valid():
                riskserializer.save()
                return Response(riskserializer.data)
            return Response(riskserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    

    def delete(self, request, pk, format=None):
        try:
            risk = Risk.objects.get(
                id=pk
            )
            risk.delete()
            return Response({"status": "success", "message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)


class IssueView(AllPostsMixin, APIView):
    model = Issue
    serializer = IssueSerializer
    
    def get(self,request, pk):
        try:
            result = Issue.objects.filter(
                report_id=pk
            )
            issueserializer = IssueSerializer(result,many = True)
            return Response(issueserializer.data)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
        

    def put(self, request, format=None):
        try:
            issue = Issue.objects.get(
                user_id=request.user.id,
                project_id=request.data["project_id"],
                report_id=request.data["report_id"],
                issue_id=request.data["issue_id"]
            )
            issueserializer = IssueSerializer(issue, data=request.data)
            if issueserializer.is_valid():
                issueserializer.save()
                return Response(issueserializer.data)
            return Response(issueserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    

    def delete(self, request, pk, format=None):
        try:
            issue = Issue.objects.get(
                id=pk
            )
            issue.delete()
            return Response({"status": "success", "message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    


class AssumptionView(AllPostsMixin, APIView):
    model = Assumption
    serializer = AssumptionSerializer
    

    def get(self, request, pk):
        try:
            result = Assumption.objects.filter(
                report_id=pk
            )
            assumptionserializer = AssumptionSerializer(result,many = True)
            return Response(assumptionserializer.data)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
        

    def put(self, request, format=None):
        try:
            assumption = Assumption.objects.get(
                user_id=request.user.id,
                project_id=request.data["project_id"],
                report_id=request.data["report_id"],
                assumption_id=request.data["assumption_id"]
            )
            assumptionserializer = AssumptionSerializer(assumption, data=request.data)
            if assumptionserializer.is_valid():
                assumptionserializer.save()
                return Response(assumptionserializer.data)
            return Response(assumptionserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    

    def delete(self, request, pk, format=None):
        try:
            assumption = Assumption.objects.get(
                id=pk
            )
            assumption.delete()
            return Response({"status": "success", "message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    

class DependencyView(AllPostsMixin, APIView):
    model = Dependency
    serializer = DependencySerializer
    
    def get(self, request, pk):
        try:
            result = Dependency.objects.filter(
               report_id=pk
            )
            dependancyserializer = DependencySerializer(result,many = True)
            return Response(dependancyserializer.data)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
        

    def put(self, request, format=None):
        try:
            dependancy = Dependency.objects.get(
                user_id=request.user.id,
                project_id=request.data["project_id"],
                report_id=request.data["report_id"],
                dependency_id=request.data["dependency_id"]
            )
            dependancyserializer = DependencySerializer(dependancy, data=request.data)
            if dependancyserializer.is_valid():
                dependancyserializer.save()
                return Response(dependancyserializer.data)
            return Response(dependancyserializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    

    def delete(self, request, pk, format=None):
        try:
            dependancy = Dependency.objects.get(
                id=pk
            )
            dependancy.delete()
            return Response({"status": "success", "message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)