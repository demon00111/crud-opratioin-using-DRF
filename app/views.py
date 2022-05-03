import io
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .models import Student
from django.views.decorators.csrf import csrf_exempt 
from .serializer import StudentSerializer

# Create your views here.




@csrf_exempt
def student(request):
    if request.method == "GET":
        json_data = request.body
        stream =io.BytesIO(json_data)
        python_data= JSONParser().parse(stream)
        id= python_data.get('id')
        # data = Student.objects.all()
        # id = data.id
        # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",id)

        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return JsonResponse(serializer.data)
        # elif id :


        else:
            stu = Student.objects.all()
            serializer= StudentSerializer(stu , many=True)
            return JsonResponse(serializer.data,safe=False)
    

   
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data= JSONParser().parse(stream)
        serializer= StudentSerializer(data= python_data)
        if serializer.is_valid(): 
            serializer.save()
            
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, safe=False)

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data= JSONParser().parse(stream)
        id = python_data.get("id")
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=python_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response_msg = {'msg': 'data updated successfully!!!!!'}
            return JsonResponse(response_msg,safe=False)
        return JsonResponse(serializer.errors,safe=False)

    if request.method == 'DELETE':
        json_data=request.body
        stream= io.BytesIO(json_data)
        python_data= JSONParser().parse(stream)
        id = python_data.get("id")
        if id is not None:
            
            stu= Student.objects.get(id=id)
            stu.delete()
            response_msg= {'msg':'Data deleted !!!!!!'}
            return JsonResponse(response_msg,safe=False)
        

        response_msg= {'msg':'Please enter id !!!!!!'}
        return JsonResponse(response_msg,safe=False)