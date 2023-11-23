from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import viewsets, status
from project_plan.renderers import ProjectPlanRenderer
from django.shortcuts import get_object_or_404
    
class ProjectDetailViewSet(viewsets.ViewSet):
    renderer_classes = [ProjectPlanRenderer]
    def list(self, request):
        proj = Project.objects.filter(user_id=request.user.id)
        serializer = ProjectSerializer(proj, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            proj = Project.objects.get(pk=pk)
            serializer = ProjectSerializer(proj)
            return Response(serializer.data)
        except Project.DoesNotExist:
            return Response({"error": "Project does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Created", "Data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            proj = Project.objects.get(pk=pk)
            serializer = ProjectSerializer(proj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Complete update Successful"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Project.DoesNotExist:
            return Response({"error": "Project does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        try:
            proj = Project.objects.get(pk=pk)
            serializer = ProjectSerializer(proj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Partial update Successful"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Project.DoesNotExist:
            return Response({"error": "Project does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            proj = Project.objects.get(pk=pk)
            proj.delete()
            return Response({"msg": "Deletion Successful"})
        except Project.DoesNotExist:
            return Response({"error": "Project does not exist"}, status=status.HTTP_404_NOT_FOUND)

class WeeklyReportViewSet(viewsets.ViewSet):
    renderer_classes = [ProjectPlanRenderer]
    def list(self, request):
        report = WeeklyReport.objects.all()
        serializer = WeeklyReportSerializer(report, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            report = WeeklyReport.objects.get(pk=pk)
            serializer = WeeklyReportSerializer(report)
            return Response(serializer.data)
        except WeeklyReport.DoesNotExist:
            return Response({"error": "Weekly Report does not exist"}, status=status.HTTP_404_NOT_FOUND)


    def create(self, request):
        serializer = WeeklyReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Created", "Data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            report = WeeklyReport.objects.get(pk=pk)
            serializer = WeeklyReportSerializer(report, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Complete update Successful"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except WeeklyReport.DoesNotExist:
            return Response({"error": "Weekly Report does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        try:
            report = WeeklyReport.objects.get(pk=pk)
            serializer = WeeklyReportSerializer(report, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Partial update Successful"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except WeeklyReport.DoesNotExist:
            return Response({"error": "Weekly Report does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            report = WeeklyReport.objects.get(pk=pk)
            report.delete()
            return Response({"msg": "Deletion Successful"})
        except WeeklyReport.DoesNotExist:
            return Response({"error": "Weekly Report does not exist"}, status=status.HTTP_404_NOT_FOUND)

class ProjectStatusViewSet(viewsets.ViewSet):
    renderer_classes = [ProjectPlanRenderer]
    def list(self, request):
        projstatus = ProjectStatus.objects.all()
        serializer = ProjectStatusSerializer(projstatus, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
           
            projstatus = ProjectStatus.objects.get(report=pk)
            serializer = ProjectStatusSerializer(projstatus)
            return Response(serializer.data)
        except ProjectStatus.DoesNotExist:
            return Response({"error": "Project Status does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = ProjectStatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Created", "Data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            projstatus = ProjectStatus.objects.get(pk=pk)
            serializer = ProjectStatusSerializer(projstatus, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Complete update Successful"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ProjectStatus.DoesNotExist:
            return Response({"error": "Project Status does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        try:
            projstatus = ProjectStatus.objects.get(pk=pk)
            serializer = ProjectStatusSerializer(projstatus, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Partial update Successful"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ProjectStatus.DoesNotExist:
            return Response({"error": "Project Status does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            projstatus = ProjectStatus.objects.get(pk=pk)
            projstatus.delete()
            return Response({"msg": "Deletion Successful"})
        except ProjectStatus.DoesNotExist:
            return Response({"error": "Project Status does not exist"}, status=status.HTTP_404_NOT_FOUND)

class PhaseWiseTimelineViewSet(viewsets.ViewSet):
    renderer_classes = [ProjectPlanRenderer]
    def list(self, request):
        phasetimeline = PhaseWiseTimeline.objects.all()
        serializer = PhaseWiseTimelineSerializer(phasetimeline, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
           
            phasetimeline = PhaseWiseTimeline.objects.get(report=pk)
            serializer = PhaseWiseTimelineSerializer(phasetimeline)
            return Response(serializer.data)
        except PhaseWiseTimeline.DoesNotExist:
            return Response({"error": "Phase Wise Timeline does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = PhaseWiseTimelineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Created", "Data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            phasetimeline = PhaseWiseTimeline.objects.get(pk=pk)
            serializer = PhaseWiseTimelineSerializer(phasetimeline, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Complete update Successful"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PhaseWiseTimeline.DoesNotExist:
            return Response({"error": "Phase Wise Timeline does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        try:
            phasetimeline = PhaseWiseTimeline.objects.get(pk=pk)
            serializer = PhaseWiseTimelineSerializer(phasetimeline, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Partial update Successful"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except PhaseWiseTimeline.DoesNotExist:
            return Response({"error": "Phase Wise Timeline does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            phasetimeline = PhaseWiseTimeline.objects.get(pk=pk)
            phasetimeline.delete()
            return Response({"msg": "Deletion Successful"})
        except PhaseWiseTimeline.DoesNotExist:
            return Response({"error": "Project Status does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
class PhaseViewSet(viewsets.ViewSet):
    renderer_classes = [ProjectPlanRenderer]
    def list(self, request):
        phasetimeline = Phase.objects.all()
        serializer = PhaseSerializer(phasetimeline, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
           
            phasetimeline = Phase.objects.filter(timeline_id=pk)
            serializer = PhaseSerializer(phasetimeline, many=True)
            return Response(serializer.data)
        except Phase.DoesNotExist:
            return Response({"error": "Phase does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = PhaseSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Created", "Data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            phasetimeline = Phase.objects.get(pk=pk)
            serializer = PhaseSerializer(phasetimeline, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Complete update Successful"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Phase.DoesNotExist:
            return Response({"error": "Phase Wise Timeline does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        try:
            phasetimeline = Phase.objects.get(pk=pk)
            serializer = PhaseSerializer(phasetimeline, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Partial update Successful"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Phase.DoesNotExist:
            return Response({"error": "Phase Wise Timeline does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            phasetimeline = Phase.objects.get(pk=pk)
            phasetimeline.delete()
            return Response({"msg": "Deletion Successful"})
        except Phase.DoesNotExist:
            return Response({"error": "Project Status does not exist"}, status=status.HTTP_404_NOT_FOUND)

class TaskToDoViewSet(viewsets.ViewSet):
    renderer_classes = [ProjectPlanRenderer]
    def list(self, request):
        todo = TaskToDo.objects.all()
        serializer = TaskToDoSerializers(todo, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            todo = TaskToDo.objects.get(pk=pk)
            serializer = TaskToDoSerializers(todo)
            return Response(serializer.data)
        except TaskToDo.DoesNotExist:
            return Response({"error": "Task To Do does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = TaskToDoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Created", "Data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            todo = TaskToDo.objects.get(pk=pk)
            serializer = TaskToDoSerializers(todo, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Complete update Successful"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except TaskToDo.DoesNotExist:
            return Response({"error": "Task To Do does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        try:
            todo = TaskToDo.objects.get(pk=pk)
            serializer = TaskToDoSerializers(todo, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Partial update Successful"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except TaskToDo.DoesNotExist:
            return Response({"error": "Task To Do does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            todo = TaskToDo.objects.get(pk=pk)
            todo.delete()
            return Response({"msg": "Deletion Successful"})
        except TaskToDo.DoesNotExist:
            return Response({"error": "Task To Do does not exist"}, status=status.HTTP_404_NOT_FOUND)

class AccomplishmentViewSet(viewsets.ViewSet):
    renderer_classes = [ProjectPlanRenderer]
    def list(self, request):
        accomplishment = Accomplishment.objects.all()
        serializer = AccomplishmentSerializers(accomplishment, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            
            accomplishment = Accomplishment.objects.get(report=pk)
            serializer = AccomplishmentSerializers(accomplishment)
            return Response(serializer.data)
        except Accomplishment.DoesNotExist:
            return Response({"error": "Accomplishment does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = AccomplishmentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Created", "Data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            accomplishment = Accomplishment.objects.get(pk=pk)
            serializer = AccomplishmentSerializers(accomplishment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Complete update Successful"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Accomplishment.DoesNotExist:
            return Response({"error": "Accomplishment does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        try:
            accomplishment = Accomplishment.objects.get(pk=pk)
            serializer = AccomplishmentSerializers(accomplishment, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Partial update Successful"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Accomplishment.DoesNotExist:
            return Response({"error": "Accomplishment does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            accomplishment = Accomplishment.objects.get(pk=pk)
            accomplishment.delete()
            return Response({"msg": "Deletion Successful"})
        except Accomplishment.DoesNotExist:
            return Response({"error": "Accomplishment does not exist"}, status=status.HTTP_404_NOT_FOUND)

class RiskViewSet(viewsets.ViewSet):
    renderer_classes = [ProjectPlanRenderer]
    def list(self, request):
        risk = Risk.objects.all()
        serializer = RiskSerializer(risk, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
           
            risk = Risk.objects.get(report=pk)
            serializer = RiskSerializer(risk)
            return Response(serializer.data)
        except Risk.DoesNotExist:
            return Response({"error": "Risk does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = RiskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Created", "Data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            risk = Risk.objects.get(pk=pk)
            serializer = RiskSerializer(risk, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Complete update Successful"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Risk.DoesNotExist:
            return Response({"error": "Risk does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        try:
            risk = Risk.objects.get(pk=pk)
            serializer = RiskSerializer(risk, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Partial update Successful"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Risk.DoesNotExist:
            return Response({"error": "Risk does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            risk = Risk.objects.get(pk=pk)
            risk.delete()
            return Response({"msg": "Deletion Successful"})
        except Risk.DoesNotExist:
            return Response({"error": "Risk does not exist"}, status=status.HTTP_404_NOT_FOUND)

class IssueViewSet(viewsets.ViewSet):
    renderer_classes = [ProjectPlanRenderer]
    def list(self, request):
        issue = Issue.objects.all()
        serializer = IssueSerializer(issue, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            
            issue = Issue.objects.get(report=pk)
            serializer = IssueSerializer(issue)
            return Response(serializer.data)
        except Issue.DoesNotExist:
            return Response({"error": "Issue does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = IssueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Created", "Data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            issue = Issue.objects.get(pk=pk)
            serializer = IssueSerializer(issue, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Complete update Successful"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Issue.DoesNotExist:
            return Response({"error": "Issue does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        try:
            issue = Issue.objects.get(pk=pk)
            serializer = IssueSerializer(issue, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Partial update Successful"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Issue.DoesNotExist:
            return Response({"error": "Issue does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            issue = Issue.objects.get(pk=pk)
            issue.delete()
            return Response({"msg": "Deletion Successful"})
        except Issue.DoesNotExist:
            return Response({"error": "Issue does not exist"}, status=status.HTTP_404_NOT_FOUND)

class AssumptionViewSet(viewsets.ViewSet):
    renderer_classes = [ProjectPlanRenderer]
    def list(self, request):
        assumption = Assumption.objects.all()
        serializer = AssumptionSerializer(assumption, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            
            assumption = Assumption.objects.get(report=pk)
            serializer = AssumptionSerializer(assumption)
            return Response(serializer.data)
        except Assumption.DoesNotExist:
            return Response({"error": "Assumption does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = AssumptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Created", "Data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            assumption = Assumption.objects.get(pk=pk)
            serializer = AssumptionSerializer(assumption, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Complete update Successful"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Assumption.DoesNotExist:
            return Response({"error": "Assumption does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        try:
            assumption = Assumption.objects.get(pk=pk)
            serializer = AssumptionSerializer(assumption, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Partial update Successful"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Assumption.DoesNotExist:
            return Response({"error": "Assumption does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            assumption = Assumption.objects.get(pk=pk)
            assumption.delete()
            return Response({"msg": "Deletion Successful"})
        except Assumption.DoesNotExist:
            return Response({"error": "Assumption does not exist"}, status=status.HTTP_404_NOT_FOUND)

class DependencyViewSet(viewsets.ViewSet):
    renderer_classes = [ProjectPlanRenderer]
    def list(self, request):
        dependency = Dependency.objects.all()
        serializer = DependencySerializer(dependency, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            
            dependency = Dependency.objects.get(report=pk)
            serializer = DependencySerializer(dependency)
            return Response(serializer.data)
        except Dependency.DoesNotExist:
            return Response({"error": "Dependency does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request):
        serializer = DependencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Created", "Data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        try:
            dependency = Dependency.objects.get(pk=pk)
            serializer = DependencySerializer(dependency, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Complete update Successful"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Dependency.DoesNotExist:
            return Response({"error": "Dependency does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def partial_update(self, request, pk=None):
        try:
            dependency = Dependency.objects.get(pk=pk)
            serializer = DependencySerializer(dependency, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg": "Partial update Successful"}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Dependency.DoesNotExist:
            return Response({"error": "Dependency does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk=None):
        try:
            dependency = Dependency.objects.get(pk=pk)
            dependency.delete()
            return Response({"msg": "Deletion Successful"})
        except Dependency.DoesNotExist:
            return Response({"error": "Dependency does not exist"}, status=status.HTTP_404_NOT_FOUND)
