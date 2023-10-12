from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TaskToDo,WeeklyReport,Accomplishment
from .serializers import TaskToDoSerializers,WeeklyReportSerializers,AccomplishmentSerializers

class WeeklyReportID(APIView):
    def get(self,request,id):
        try:
            result = WeeklyReport.objects.get(ReportID=id)
            serializers = WeeklyReportSerializers(result)
            return Response({'status': 'success', "Employee": serializers.data}, status=200)
        except Exception as e:
            response = JsonResponse({"meassage": "Record is not found"})
            return response
            

# Create your views here.
class WeeklyReportView(APIView):
    def get(self,request):
        print(request)
        result = WeeklyReport.objects.all()
        serializers = WeeklyReportSerializers(result,many = True)
        return Response(serializers.data)
        
    def post(self, request):
        serializer = WeeklyReportSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, id):
        result = WeeklyReport.objects.get(ReportID=id)
        serializer = WeeklyReportSerializers(result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
        
        
    def delete(self, request, id):
        result = WeeklyReport.objects.filter(ReportID=id) 
        result.delete()  
        return Response({"status": "success", "data": "Record Deleted"})  

class TaskToDoView(APIView):
    def get(self,request):
        result = TaskToDo.objects.all()
        serializers = TaskToDoSerializers(result,many = True)
        return Response(serializers.data)

    def post(self, request):
        serializer = TaskToDoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, id):
        result = TaskToDo.objects.get(TaskID=id)
        serializer = TaskToDoSerializers(result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
             

    def delete(self, request, id):
        try:
            result =TaskToDo.objects.filter(TaskID=id)
            result.delete()
            return Response({"status": "success", "message": "Record Deleted"})
        except Exception as e:
            response = JsonResponse({"meassage": "Record is not found"})
            return response
        
 
        
class AccomplishmentView(APIView):
    def get(self,request):
        result = Accomplishment.objects.all()
        serializers = AccomplishmentSerializers(result,many = True)
        return Response(serializers.data)

    def post(self, request):
        serializer = AccomplishmentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request,id):
        result = Accomplishment.objects.get(AccomplishmentID=id)
        serializer = AccomplishmentSerializers(result, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})
        
    def delete(self, request, id):
        try:
            result =Accomplishment.objects.filter(AccomplishmentID=id)
            result.delete()
            return Response({"status": "success", "message": "Record Deleted"})
        except Exception as e:
            response = JsonResponse({"meassage": "Record is not found"})
            return response