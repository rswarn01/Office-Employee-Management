from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, "index.html")


def add_emp(request):  # sourcery skip: extract-method
    try:
        if request.method != "POST":
            return render(request, "add_emp.html")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        department = int(request.POST.get("department"))
        role = int(request.POST.get("role"))
        salary = int(request.POST.get("salary"))
        phone = int(request.POST.get("phone"))

        new_emp = Employee(
            first_name=first_name,
            last_name=last_name,
            department_id=department,
            role_id=role,
            salary=salary,
            phone=phone,
        )
        new_emp.save()
        return HttpResponse("Emplyee created successfully")
    except Exception as e:
        return HttpResponse("An error occured while creating employee", e)


def all_emp(request):
    employee = Employee.objects.all()
    context = {"employees": employee}
    return render(request, "all_emp.html", context)


def remove_emp(request, emp_id=0):
    if emp_id:
        emp_to_be_deleted = Employee.objects.get(emp_id=emp_id)
        emp_to_be_deleted.delete()
        return HttpResponse("Employee deleted")
    else:
        emps = Employee.objects.all()
        context = {"employees": emps}
    return render(request, "remove_emp.html", context)


def filter_emp(request):
    try:
        if request.method == "POST":
            return _extracted_from_filter_emp(request)
        else:
            return render(request, "filter_emp.html")
    except Exception as e:
        return HttpResponse("An error occured while filtering employee", e)


# TODO Rename this here and in `filter_emp`
def _extracted_from_filter_emp(request):
    name = request.POST.get("name")
    department = request.POST.get("department")
    role = request.POST.get("role")

    emp_details = Employee.objects.all()
    if name:
        emps = emp_details.filter(
            Q(first_name__icontains=name) | Q(last_name__icontains=name)
        )
    if department:
        emps = emp_details.filter(department__name__icontains=department)
    if role:
        emps = emp_details.filter(role__name__icontains=role)
    context = {"employees": emps}

    return render(request, "all_emp.html", context)


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username)
        if not user.exists():
            messages.error(request, "Invalid username")
            return redirect("/login/")

        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid credential")
            return redirect("/login/")

        else:
            login(request, user)
            return redirect("/")

    return render(request, "login.html")


def register_page(request):
    if request.method != "POST":
        return render(request, "register.html")
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    username = request.POST.get("username")
    password = request.POST.get("password")

    user = User.objects.filter(username=username)
    if user.exists():
        messages.info(request, "Email already exists")
        return redirect("/register/")

    user = User.objects.create(
        first_name=first_name, last_name=last_name, username=username
    )
    user.set_password(password)
    user.save()
    messages.info(request, "User registration done")

    return redirect("/register/")


def logout_page(request):
    logout(request)
    return redirect("/login/")
