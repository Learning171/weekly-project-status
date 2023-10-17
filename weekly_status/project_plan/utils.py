from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_list_or_404

class AllViewsMixin:
    model = None
    serializer = None

    # def get(self, request):
    #     # result = Account.objects.all()
    #     result = get_list_or_404(self.model)
    #     serializer = self.serializer(result, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        serializer = self.serializer(data=data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'status': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)