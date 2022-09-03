from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, request
from django.shortcuts import render, redirect

# Create your views here.
import das
from akshayapp.form import StudentForm
from akshayapp.models import Akshay, Bike, Student, college


def home(request):
    return HttpResponse("hello world")
def car(request):
    z=Akshay.objects.get()
    return render(request,'das.html',{'athena':z})


def sree(request):
    a=Bike.objects.all()
    return render(request,'das.html',{'adi':a})

def register(request):
    if request.method=='GET':
        return render(request,'reg.html')
    else:
        name=request.POST.get('name')
        age=request.POST.get('age')
        desi=request.POST.get('designation')
        sal=request.POST.get('salary')
        Student.objects.create(name=name,age=age,designation=desi,salary=sal)
        return render(request,'reg.html')
    #for display

def emp(request):
        ob=Student.objects.all()
        return render(request,'reg.html',{'ob':ob})
def insert(request):
        if request.method=='GET':
            ob=Student()
            return render(request,'new.html',{'ob':ob})
        else:
            f=StudentForm(request.POST)
            if f.is_valid():
                f.save()
            return redirect('akshayapp:emp')
def update(request,id):
        if request.method=="GET":
            ob=Student.objects.get(id=id)
            return render(request,'update.html',{'ob':ob})
        else:
            name=request.POST.get('name')
            age=request.POST.get('age')
            desi=request.POST.get('designation')
            sal=request.POST.get('salary')
            Student.objects.filter(id=id).update(name=name,age=age,designation=desi,salary=sal)
            return redirect('akshayapp:emp')
def delete(request,id):
            Student.objects.get(id=id).delete()
            return redirect('akshayapp:emp')
def display(request):
    object = college.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(object, 2)
    try:
        users = paginator.page(page)

    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'page.html', {'users': users})





