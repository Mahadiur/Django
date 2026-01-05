# from django.http import HttpResponse
from django.shortcuts import render
from Employee.models import employee

def home(request):
    emploee_list = employee.objects.all()
    employee_context = {
        'employees': emploee_list
    }
    print(employee_context)
    return render(request, 'home.html', employee_context)