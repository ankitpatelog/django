from students.models import Students
from employees.models import Employee
from rest_framework import serializers

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"
        
class  EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__" 
