from django.shortcuts import render_to_response

from django.http import HttpResponse
from rest_framework import serializers
from rest_framework import viewsets
from students.serializers import StudentSerializer
from .models import Student

class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

def index(request):
     return render_to_response('index.html')
