from django.shortcuts import render
from students.models import Students
from .serializers import StudentSerializers
from rest_framework.response import Response 
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.

# def studentsView(request):
#     student = Students.objects.all()
#     # print(student)
#     # now directly printing the student not work as it expects the dictionary but we 
#     # passing the json format which is not allowed
    
#     # so we now serialize the data into the readable format
#     # now are passing the student lsit
#     student_list = list(student.values())
#     return JsonResponse(student_list , safe=False)



# now using serializers for the data conversion 

@api_view(['GET','POST'])
def studentsView(request):

    # GET
    if request.method == 'GET':
        student = Students.objects.all()
        student_list = StudentSerializers(student, many=True)
        return Response(student_list.data, status=status.HTTP_200_OK)

    # POST
    elif request.method == 'POST':
        serialized_data = StudentSerializers(data=request.data)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)

        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def studentsDetails(request, pk):

    try:
        student = Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # GET single student
    if request.method == 'GET':
        serializer = StudentSerializers(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # UPDATE student
    elif request.method == 'PUT':
        serializer = StudentSerializers(student, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE student
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
