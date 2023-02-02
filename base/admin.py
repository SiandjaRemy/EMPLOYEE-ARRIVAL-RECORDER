from django.contrib import admin
from .models import Supervisor, Employee, Company, ArrivalTime

# Register your models here.

class SupervisorAdmin(admin.ModelAdmin):
    list_display = ['supervisor_name']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["employee_name", "employee_company", "employee_position"]

class CompanyAdmin(admin.ModelAdmin):
    list_display = ["company_name", "slug"]
    prepopulated_fields = {"slug": ("company_name", )}

class ArrivalTimeAdmin(admin.ModelAdmin):
    list_display = ["employee_name", "employee_arrival"]



admin.site.register(Supervisor, SupervisorAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(ArrivalTime, ArrivalTimeAdmin)

