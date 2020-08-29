from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.decorators import action
from .services import generator


class ExpensesView(viewsets.GenericViewSet):

    @action(detail=True, methods=['post'])
    def generator(self, request):
        print(request.data)
        total = request.data.get("total")
        distributed_count = request.data.get("distributed_count")
        variance = request.data.get("variance")
        result = {"generator": 1}
        return Response(result)

    @action(detail=True, methods=['get'])
    def generator2(self, request):
        result = {"generator2": 2}
        return Response(result)
