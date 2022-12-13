from django.contrib import admin
from .models import Employee, EmpDetails
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','eid','name','city']


@admin.register(EmpDetails)
class EmpDetailsAdmin(admin.ModelAdmin):
    list_display=['phone', 'state', 'employee']