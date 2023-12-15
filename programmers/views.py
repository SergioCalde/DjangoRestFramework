from django.shortcuts import render
from .models import Programmer
from rest_framework import permissions, viewsets
from .serializers import ProgrammerSerializer

# Create your views here.
class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
