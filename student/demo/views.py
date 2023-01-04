from django.shortcuts import render, HttpResponse
from .models import student
from django.db.models import Q



def index(request):
    return render(request, 'index.html')


def all_stu(request):
    stu = student.objects.all()
    context = {
        'stu': stu
    }
    # print(context)
    return render(request, 'view_all_stu.html', context)


def add_stu(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        position = request.POST['position']
        
        
        new_stu = student(name = name, age = age , position = position)
        new_stu.save()
        return HttpResponse('student added Successfully')
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


def filter_stu(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        position = request.POST['position']
        stu= student.objects.all()
        if name:
            stu = stu.filter(Q(name__icontains = name) )
        if age:
            stu = stu.filter(age__icontains = age)
        if position:
            stu = stu.filter(position__icontains = position)

        context = {
            'stu': stu
        }
        return render(request, 'view_all_stu.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_stu.html')
    else:
        return HttpResponse('An Exception Occurred')