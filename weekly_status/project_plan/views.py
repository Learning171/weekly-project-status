from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

class AllViewsMixin:
    model = None
    serializer = None

    def post(self, request):
        data = request.data
        serializer = self.serializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class ProjectView(AllViewsMixin, APIView):
    model = Project
    serializer = ProjectSerializer

    def get(self, request):
        try:
            result = Project.objects.filter(user_id=request.user.id)
            serializer = self.serializer(result, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
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
    

    def delete(self, request, format=None):
        try:
            project = Project.objects.get(
                user_id=request.user.id,
                id=request.data["project_id"]
            )
            project.delete()
            return Response({"status": "success", "message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)


class ProjectDetailView(APIView):
    def get(self, request):
        try:
            result = Project.objects.get(
                user_id=request.user.id,
                id=request.data["project_id"]
            )
            serializer = self.serializer(result)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    

class ProjectWeeklyReportView(AllViewsMixin, APIView):
    model = WeeklyReport
    serializer = WeeklyReportSerializer

    def get(self, request):
        try:
            result = WeeklyReport.objects.filter(
                project_id=request.data["project_id"]
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
    

    def delete(self, request, format=None):
        try:
            weeklyreport = WeeklyReport.objects.get(
                id=request.data["report_id"]
            )
            weeklyreport.delete()
            return Response({"status": "success", "message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    

class AllWeeklyReportView(APIView):
    model = WeeklyReport
    serializer = WeeklyReportSerializer

    def get(self, request):
        try:
            user_projects = Project.objects.filter(user_id=request.user.id)
            user_projects_ids = [project.id for project in user_projects]
            result = WeeklyReport.objects.filter(project_id__in=user_projects_ids)
            weeklyreportserializer = WeeklyReportSerializer(result, many=True)
            return Response(weeklyreportserializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)


class ProjectStatusView(AllViewsMixin, APIView):
    model = ProjectStatus
    serializer = ProjectStatusSerializer

    def get(self, request):
        try:
            result = ProjectStatus.objects.filter(
                report=request.data["report_id"]
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
    

    def delete(self, request, format=None):
        try:
            projectstatus = ProjectStatus.objects.get(
                id=request.data["status_id"]
            )
            projectstatus.delete()
            return Response({"status": "success", "message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    


class PhaseWiseTimelineView(AllViewsMixin, APIView):
    model = PhaseWiseTimeline
    serializer = PhaseWiseTimelineSerializer

    def get(self, request):
        try:
            result = PhaseWiseTimeline.objects.filter(
                report_id=request.data["report_id"],
                id=request.data["timeline_id"]
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
    

    def delete(self, request, format=None):
        try:
            phasewisetimeline = PhaseWiseTimeline.objects.get(
                id=request.data["timeline_id"]
            )
            phasewisetimeline.delete()
            return Response({"status": "success", "message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    


class PhaseView(AllViewsMixin, APIView):
    model = Phase
    serializer = PhaseSerializer

    def get(self, request):
        try:
            result = Phase.objects.filter(
                user_id=request.user.id,
                project_id=request.data["project_id"],
                report_id=request.data["report_id"],
                timeline_id=request.data["timeline_id"]
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
    

    def delete(self, request, format=None):
        try:
            phase = Phase.objects.get(
                user_id=request.user.id,
                project_id=request.data["project_id"],
                report_id=request.data["report_id"],
                timeline_id=request.data["timeline_id"],
                phase_name=request.data["phase_name"]
            )
            phase.delete()
            return Response({"status": "success", "message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    


class TaskToDoView(AllViewsMixin, APIView):
    model = TaskToDo
    serializer = TaskToDoSerializers

    def get(self,request):
        try:
            result = TaskToDo.objects.filter(
                user_id=request.user.id,
                project_id=request.data["project_id"],
                report_id=request.data["report_id"]
            )
            serializers = TaskToDoSerializers(result,many = True)
            return Response(serializers.data)
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
            serializer = TaskToDoSerializers(result, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})
            return Response({"status": "error", "data": serializer.errors})
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
             

    def delete(self, request):
        try:
            result =TaskToDo.objects.get(
                id=request.data["tasktodo_id"]
            )
            result.delete()
            return Response({"status": "success", "message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"status": "error", "meassage": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
        
 
        
class AccomplishmentView(AllViewsMixin, APIView):
    model = Accomplishment
    serializer = AccomplishmentSerializers

    def get(self,request):
        try:
            result = Accomplishment.objects.filter(
                user_id=request.user.id,
                project_id=request.data["project_id"],
                report_id=request.data["report_id"]
            )
            serializers = AccomplishmentSerializers(result,many = True)
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
            serializer = AccomplishmentSerializers(result, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "success", "data": serializer.data})
            return Response({"status": "error", "data": serializer.errors})
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
        
    def delete(self, request):
        try:
            result =Accomplishment.objects.get(
            user_id=request.user.id,
            project_id=request.data["project_id"],
            report_id=request.data["report_id"],
            accomplishment_id=request.data["accomplishment_id"]
        )
            result.delete()
            return Response({"status": "success", "message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"status": "error", "meassage": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
        

class RiskView(AllViewsMixin, APIView):
    model = Risk
    serializer = RiskSerializer
    
    def get(self,request):
        try:
            result = Risk.objects.filter(
                user_id=request.user.id,
                project_id=request.data["project_id"],
                report_id=request.data["report_id"]
            )
            serializers = RiskSerializer(result,many = True)
            return Response(serializers.data)
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
            serializer = RiskSerializer(risk, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    

    def delete(self, request, format=None):
        try:
            risk = Risk.objects.get(
                user_id=request.user.id,
                project_id=request.data["project_id"],
                report_id=request.data["report_id"],
                risk_id=request.data["risk_id"]
            )
            risk.delete()
            return Response({"status": "success", "message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)




class IssueView(AllViewsMixin, APIView):
    model = Issue
    serializer = IssueSerializer
    
    def get(self,request):
        try:
            result = Issue.objects.filter(
                user_id=request.user.id,
                project_id=request.data["project_id"],
                report_id=request.data["report_id"]
            )
            serializers = IssueSerializer(result,many = True)
            return Response(serializers.data)
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
            serializer = IssueSerializer(issue, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    

    def delete(self, request, format=None):
        try:
            issue = Issue.objects.get(
                user_id=request.user.id,
                project_id=request.data["project_id"],
                report_id=request.data["report_id"],
                issue_id=request.data["issue_id"]
            )
            issue.delete()
            return Response({"status": "success", "message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    


class AssumptionView(AllViewsMixin, APIView):
    model = Assumption
    serializer = AssumptionSerializer
    

    def get(self,request):
        try:
            result = Assumption.objects.filter(
                user_id=request.user.id,
                project_id=request.data["project_id"],
                report_id=request.data["report_id"]
            )
            serializers = AssumptionSerializer(result,many = True)
            return Response(serializers.data)
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
            serializer = AssumptionSerializer(assumption, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    

    def delete(self, request, format=None):
        try:
            assumption = Assumption.objects.get(
                user_id=request.user.id,
                project_id=request.data["project_id"],
                report_id=request.data["report_id"],
                assumption_id=request.data["assumption_id"]
            )
            assumption.delete()
            return Response({"status": "success", "message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    

class DependencyView(AllViewsMixin, APIView):
    model = Dependency
    serializer = DependencySerializer
    
    def get(self,request):
        try:
            result = Dependency.objects.filter(
                user_id=request.user.id,
                project_id=request.data["project_id"],
                report_id=request.data["report_id"]
            )
            serializers = DependencySerializer(result,many = True)
            return Response(serializers.data)
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
            serializer = DependencySerializer(dependancy, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)
    

    def delete(self, request, format=None):
        try:
            dependancy = Dependency.objects.get(
                user_id=request.user.id,
                project_id=request.data["project_id"],
                report_id=request.data["report_id"],
                dependency_id=request.data["dependency_id"]
            )
            dependancy.delete()
            return Response({"status": "success", "message": "Record Deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"status": "error", "message": f"{e}"}, status=status.HTTP_404_NOT_FOUND)