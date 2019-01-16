from django.shortcuts import render
from .models import UserModel


def dashboard(request):

    return render(request, "dashboard/dashboard.html", {
        "user": request.user,
        "location": "Raleigh ",

    })


def managerdashboard(request):
    print('Admin User is here', request.user)
    list = UserModel.objects.all()
    filterList = list
    return render(request, "dashboard/managerdashboard.html", {
        "name": "managerdashboardView",
        "title": "QA Manager",
        "location": "Raleigh ",
        'list': list
    })


def myaccount(request):
    print('Requested user is ', request.user)
    myaccount = UserModel.objects.filter(
        first_name=request.user).values()
    return render(request, "myaccount/myaccount.html", {
        "user": request.user,
        "location": "Raleigh ",
        'myaccount': myaccount,

    })
