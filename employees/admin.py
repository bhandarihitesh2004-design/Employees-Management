from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'department', 'role', 'status')
    search_fields = ('employee_id', 'name', 'email', 'department', 'role')
