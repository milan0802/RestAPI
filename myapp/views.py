from django.shortcuts import render
from rest_framework import generics
from .models import Department,Employee
from .serializers import DepartmentSerializer,EmployeeSerializer
# Create your views here.

class DepartmentList(generics.ListCreateAPIView):
	queryset=Department.objects.all()
	serializer_class=DepartmentSerializer

class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=Department
	serializer_class=DepartmentSerializer

class EmployeeList(generics.ListCreateAPIView):
	queryset=Employee.objects.all()
	serializer_class=EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset=Employee
	serializer_class=EmployeeSerializer
