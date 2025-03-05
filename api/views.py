from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# Function-based view
@api_view(['GET', 'POST', 'PUT'])
def test(request):
    return Response({"message": "hiapi"})

# Class-based view
class TestAPI(APIView):
    def get(self, request):
        return Response({"message": "hiapi once"})
