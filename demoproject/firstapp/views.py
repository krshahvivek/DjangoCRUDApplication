from django.shortcuts import render, HttpResponse
from .forms import DeptForm, EmployeesForm
from django.views.decorators.csrf import csrf_exempt
from .models import Dept, Employess

# Create your views here.

@csrf_exempt
def add_employees(request):
    if request.method == 'POST':
        emp = EmployeesForm(request.POST)
        if emp.is_valid:
            emp.save()
        emp = EmployeesForm()
    else:
        emp = EmployeesForm()
    empData = Employess.objects.all()
    return render(request, 'main/create-user.html', {'form':emp, 'data': empData})

@csrf_exempt
def add_dept(request):
    if request.method == 'POST':
        dept = DeptForm(request.POST)
        if dept.is_valid:
            dept.save()
        dept = DeptForm()
    else:
        dept = DeptForm()
    deptData = Dept.objects.all()
    return render(request, 'main/create-dept.html', {'form':dept, 'data':deptData})

@csrf_exempt
def delete_dept(request, id):
    if request.method == 'POST':
        dept = Dept.objects.get(pk=id)
        print('dept',dept)
        dept.delete()
    return HttpResponse('data delete')
    
@csrf_exempt
def delete_employee(request, id):
    if request.method == 'POST':
        emp = Employess.objects.get(pk=id)
        print('somes',emp)
        dept = Dept.objects.filter(code=emp.dept)
        dept.delete()
        emp.delete()
        return HttpResponse('/Data deleted')
    
@csrf_exempt
def edit_dept(request, id):
    if request.method == 'POST':
        print('::::::::::::::::::dept::::::::::::::::::::::::',dept)
        dept = Dept.objects.get(pk=id)
        update_data = DeptForm(request.POST, instance=dept)
        if update_data.is_valid():
            update_data.save()
    else:
        dept = Dept.objects.get(pk=id)
        update_data = DeptForm(instance=dept)
        print(':::::::',dept)
    return render(request, 'main/update-data.html', {'id': update_data})
    
@csrf_exempt
def edit_employee(request, id):
    if request.method == 'POST':
        emp = Employess.objects.get(pk=id)

        update_data = EmployeesForm(request.POST, instance=emp)
        print(':::::::',update_data)
        if update_data.is_valid():
            update_data.save()
    else:
        emp = Employess.objects.get(pk=id)
        update_data = EmployeesForm(instance=emp)
        print(':::::::',update_data)
    return render(request, 'main/update-data2.html', {'id': update_data})