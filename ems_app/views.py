from django.http import Http404
from django.shortcuts import render
from .models import Employee, Job


def home(request):
    employees = Employee.objects.all()

    data = {
        'employees': employees
    }

    return render(request, 'home.html', data)


def employee_detail(request, id):
    try:
        emp_detail = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        raise Http404('Employee not found')

    data = {
        'emp_detail': emp_detail
    }

    return render(request, 'employee_detail.html', data)
