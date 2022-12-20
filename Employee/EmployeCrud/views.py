from django.shortcuts import render

from .models import Employee
from django.http import JsonResponse
from django.core.files.base import ContentFile
import base64

# Create your views here.

def index(request):
    employees = Employee.objects.all()
    return render(request, 'admin/dashboard.html', {'employees': employees})

def create(request):
    return render(request, "admin/create.html")

def store(request):
     if request.method == 'POST':
        employee = Employee()
        
        employee.name = request.POST['name']
        employee.email = request.POST['email']
        employee.phone = request.POST['phone']
        
        if 'image' in request.FILES:
            image = request.FILES.get('image')
            
        
        employee.image = image
        
        employee.save()
        
        return JsonResponse({'message': 'Employee store successful', 'status_code': 201})

def edit(request, id=None):
    employe = Employee.objects.get(id = id)
    return render(request, 'admin/edit.html', {'employe': employe})

def update(request, id=None):
    if request.method == 'POST':
        employe = Employee.objects.get(id = id)
        
        employe.name = request.POST['name']
        employe.email = request.POST['email']
        employe.phone = request.POST['phone']
        
        employe.save()
        
        return JsonResponse({'message': 'Employee updated successful', 'status_code': 200})
    
def destroy(request, id=None):
    employe = Employee.objects.get(id = id)
    employe.delete()
    
    return JsonResponse({'message': 'Employee destroy successful', 'status_code': 200})
