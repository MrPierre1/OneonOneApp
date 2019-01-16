"""oneOnOne URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.task, name='task')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from dashboard import views as DashboardViews
from oneOnOne import views as oneOnOneViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', DashboardViews.dashboard, name='dashboard'),
    path('manager/', DashboardViews.managerdashboard, name='managerdashboard'),
    path('myaccount/', DashboardViews.myaccount, name='myaccount'),

    path('feedback/', oneOnOneViews.feedback, name='feedback'),
    path('tasks/', oneOnOneViews.tasks, name='tasks'),
    path('modal1/', oneOnOneViews.modal1, name='notifications'),

    # path('', DashboardViews.index, name = 'index'),

]
