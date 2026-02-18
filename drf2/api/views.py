from students.models import Students
from .serializers import StudentSerializers,EmployeeSerializers
from rest_framework.response import Response 
from rest_framework import  status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from rest_framework import mixins,generics,viewsets,filters
from employees.filters import EmployeeFilter



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



# # class based view
# # appiview handles the automatically git post request 
# class Employees(APIView):

#     def get(self, request):
#         employee = Employee.objects.all()
#         serializer = EmployeeSerializers(employee, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = EmployeeSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class employeeDetails(APIView):
#     def get(self,request,pk):
        
        
# usign mixins
# class employeeDetails(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializers
    
#     def get(self,request):
#         return self.list(request)
    
#     def post(self,request):
#         return self.create(request)
    
#     def update(self,request,pk):
#         return self.retrieve(request,pk)
    
    
# using generics

class employeeDetails(generics.ListAPIView):
    # it handles the list api automatically just give the queryset and the model serializer
    # generics.createapiview
    # generic.lsitcreateapiview
    
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    
class EmployeeDetails(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    lookup_field = 'pk'
    
    
# using viewset and routers for dynamic routing of urls

class Employeeviewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    pagination_class = CustomPagination
    # this is used as global defalut for filtering the data but it do not handle case sensitive issue
    # filterset_fields = ['designation']
    # now we use custom filter class
    
    filterset_class = EmployeeFilter
    