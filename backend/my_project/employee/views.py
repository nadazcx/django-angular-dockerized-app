from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Employee

def add_employee_function(name, department, salary, function):
    new_employee = Employee.objects.create(
        name=name,
        department=department,
        function=function,
        salary=salary
    )
    return new_employee

@csrf_exempt
def add_employee(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            department = data.get('department')
            salary = data.get('salary')
            function = data.get('function')

            if not all([name, department, salary]):
                return JsonResponse({'error': 'Missing fields in request'}, status=400)

            new_employee = add_employee_function(name, department, salary, function)
            return JsonResponse({
                'id': new_employee.id,
                'name': new_employee.name,
                'department': new_employee.department,
                'salary': new_employee.salary,
                'function': new_employee.function
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid HTTP method'}, status=405)

        
def get_employee_all(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        employee_list = []
        for employee in employees:
            employee_data = {
                'name': employee.name,
                'department': employee.department,
                'salary': employee.salary
            }
            employee_list.append(employee_data)
        return JsonResponse(employee_list, safe=False)