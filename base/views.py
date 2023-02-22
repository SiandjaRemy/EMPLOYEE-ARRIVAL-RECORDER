from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Supervisor, Company, ArrivalTime
from .forms import EmployeeForm


# Create your views here.

def index(request):
    companies = Company.objects.all()
    supervisor = Supervisor.objects.all()

    context = {
        "companies":companies,
        "supervisor":supervisor
    }
    return render(request, "index.html", context) #Company list

def addCompany(request):
    return render(request, "addcom.html")

def newCompany(request):
    if request.method == "POST":
        company_name = request.POST["company_name"]
        company_description = request.POST["company_description"]

        company = Company(company_name=company_name, company_description=company_description)
        company.save()

        return redirect("/")
    
    return render(request, "addcom.html")

def empList(request, com):
    
    employees = get_object_or_404(Employees, employee_company=com)
    
    context = {

        "employees":employees
    }
    return render(request, "index.hrml", context)


def addEmployee(request):
    return render(request, "addemp.html")


def newEmployee(request):
    company = Company.objects.filter()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to)
    else:
        form = EmployeeForm()

    return render(request, "addemp.html")
