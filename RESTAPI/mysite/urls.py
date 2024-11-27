from django.contrib import admin
from django.urls import path
from myapp.views import DepartmentList,DepartmentDetail,EmployeeList,EmployeeDetail


urlpatterns = [
    path('department',DepartmentList.as_view()),
    path('department/<int:pk>',DepartmentDetail.as_view()),
    path('employee',EmployeeList.as_view()),
    path('employee/<int:pk>',EmployeeDetail.as_view()),
    path('admin/', admin.site.urls),
]