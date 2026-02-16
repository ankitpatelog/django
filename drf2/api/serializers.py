from students.models import Students
from rest_framework import serializers

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"
        
        
