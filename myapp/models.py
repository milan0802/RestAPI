from django.db import models

# Create your models here.
class Department(models.Model):
	deptno=models.PositiveIntegerField(blank=True)
	dname=models.CharField(max_length=100,blank=True)
	location=models.CharField(max_length=100,blank=True)

	def __str__(self):
		return self.dname

class Employee(models.Model):
	# dept=models.ForeignKey(Department,on_delete=models.CASCADE)
	ename=models.CharField(max_length=100,blank=True)
	job=models.CharField(max_length=100,blank=True)
	deptno=models.PositiveIntegerField(blank=True)
	salary=models.PositiveIntegerField(blank=True)

	def __str__(self):
		return self.ename