from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),

    path("add-company", views.addCompany, name="add_company"),
    path("new-company", views.newCompany, name="new_company"),
    path("employee-list/<slug:slug>", views.empList, name="employee_list"),
    path("add-employee", views.addEmployee, name="add_employee"),
    path("new-employee", views.newEmployee, name="new_employee"),
]