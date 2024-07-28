from django.shortcuts import render
from rest_framework import generics
from .serializers import StudentSerializer
from .models import Student

# Create your views here.
class StudentCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = "pk"

    