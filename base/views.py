from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Supervisor, Company, ArrivalTime
from .forms import EmployeeForm


# Create your views here.

def index(request):
    return render(request, "index.html") #Company list

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

def empList(request, slug):
    company = get_object_or_404(Company, slug=slug)
    employee = Employee.objects.all()
    
    return render(request, "emplist.hrml")


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
