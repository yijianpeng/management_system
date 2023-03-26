# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Employee


# Create your views here.
def assign_task_view(request):
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        employee_id = request.POST.get('employee_id')
        task = get_object_or_404(Task, pk=task_id)
        employee = get_object_or_404(Employee, pk=employee_id)
        task.assigned_to = employee
        task.save()
        return redirect('admin:tasks_task_changelist')

    tasks = Task.objects.filter(assigned_to=None)
    employees = Employee.objects.all()
    return render(request, 'assign_task.html', {'tasks': tasks, 'employees': employees})
