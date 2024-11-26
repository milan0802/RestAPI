from rest_framework import serializers
from .models import Department,Employee


class DepartmentSerializer(serializers.ModelSerializer):
	class Meta:
		model=Department
		fields=('id','deptno','dname','location')

class EmployeeSerializer(serializers.ModelSerializer):
	class Meta:
		model=Employee
		fields=('id','deptno','ename','job','salary')

