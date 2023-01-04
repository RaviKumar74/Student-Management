from django.shortcuts import render, HttpResponse
from ..models import student
from rest_framework.decorators import api_view
from .serializers import studentSerializer,userSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
# from django.db.models import Q


class loginAPI(APIView):
    def post(self, request):
        try:
            data =request.data 
            serializer = userSerializer(data = data)
            if serializer.is_valid():
                username = serializer.data['username']
                password = serializer.data['password']
                user = authenticate(username = username, password = password)
                if user is None:
                    return HttpResponse("enter a valid password")

                
                refresh = RefreshToken.for_user(user)

                if user.is_verified is False:
                    return respo

                return {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    }




            

        except Exception as e:
            print(e)
            

def index(request):
    return render(request, 'index.html')



@api_view()
def all_stu(request):
    stu = student.objects.all()
    serializer = studentSerializer(stu, many = True)
    context ={
        'stu': serializer.data
    }

    return render(request, 'view_all_stu.html', context)
@api_view(['GET','POST'])
def add_stu(request):
    if request.method == 'POST':
        serializer = studentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse('student added Successfully') 
        else:
            return HttpResponse("enter correct data please") 
    elif request.method=='GET':
        return render(request, 'add_stu.html')
    else:
        return HttpResponse("An Exception Occured! student Has Not Been Added")
def remove_stu(request, stu_id = 0):
    if stu_id:
        try:
            stu_to_be_removed = student.objects.get(id=stu_id)
            stu_to_be_removed.delete()
            return HttpResponse("student Removed Successfully")
        except:
            return HttpResponse("Please Enter A Valid student ID")
    stu = student.objects.all()
    context = {
        'stu': stu
    }
    return render(request, 'remove_stu.html',context)



# def all_stu(request):
#     stu = student.objects.all()
#     context = {
#         'stu': stu
#     }
#     # print(context)
#     return render(request, 'view_all_stu.html', context)
# def add_stu(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         age = request.POST['age']
#         position = request.POST['position']
        
        
#         new_stu = student(name = name, age = age , position = position)
#         new_stu.save()
#         return HttpResponse('student added Successfully')
#     elif request.method=='GET':
#         return render(request, 'add_stu.html')
#     else:
#         return HttpResponse("An Exception Occured! student Has Not Been Added")
# def remove_stu(request, stu_id = 0):
#     if stu_id:
#         try:
#             stu_to_be_removed = student.objects.get(id=stu_id)
#             stu_to_be_removed.delete()
#             return HttpResponse("student Removed Successfully")
#         except:
#             return HttpResponse("Please Enter A Valid student ID")
#     stu = student.objects.all()
#     context = {
#         'stu': stu
#     }
#     return render(request, 'remove_stu.html',context)


# def filter_stu(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         age = request.POST['age']
#         position = request.POST['position']
#         stu= student.objects.all()
#         if name:
#             stu = stu.filter(Q(name__icontains = name) )
#         if age:
#             stu = stu.filter(age__icontains = age)
#         if position:
#             stu = stu.filter(position__icontains = position)

#         context = {
#             'stu': stu
#         }
#         return render(request, 'view_all_stu.html', context)

#     elif request.method == 'GET':
#         return render(request, 'filter_stu.html')
#     else:
#         return HttpResponse('An Exception Occurred')