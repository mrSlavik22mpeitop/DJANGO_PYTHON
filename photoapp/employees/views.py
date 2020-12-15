from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeCreate
from django.http import HttpResponse

#DataFlair
def index_employee(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employees.html', {'employees': employees})

def upload_employee(request):
    upload = EmployeeCreate()
    if request.method == 'POST':
        upload = EmployeeCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index-employee')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'employees/upload_employees.html', {'upload_employees':upload,'title':"Добавить сотрудника"})

def update_employee(request, employee_id):
    employee_id = int(employee_id)
    try:
        employee_sel = Employee.objects.get(id = employee_id)
    except Employee.DoesNotExist:
        return redirect('index-employee')
    employee_form = EmployeeCreate(request.POST or None, instance = employee_sel)
    if employee_form.is_valid():
       employee_form.save()
       return redirect('index-employee')
    return render(request, 'employees/upload_employees.html', {'upload_employees':employee_form, 'title':"Обновить сотрудника"})

def delete_employee(request, employee_id):
    employee_id = int(employee_id)
    try:
        employee_sel = Employee.objects.get(id = employee_id)
    except Employee.DoesNotExist:
        return redirect('index-employee')
    employee_sel.delete()
    return redirect('index-employee')