from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
from rest_framework.viewsets import ModelViewSet
# class ExpenseView(ModelViewSet):
#     queryset = {"test": 1}
#     return queryset

# def ExpenseView():
#     queryset = {"test": 1}
#     result = {}
#     response = Response(result, status=status.HTTP_200_OK)
#     return response

class ExpenseView(APIView):

    def get(self, request):
        result = {"test": 1}
        return Response(result)
