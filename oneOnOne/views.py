from django.shortcuts import render
from django.http import HttpResponse
from dashboard.models import TaskModel


def tasks(request):
    taskList = TaskModel.objects.all()
    # createdTaskList = TaskModel.objects.get(creator_name='JP')
    # myTaskList = TaskModel.objects.filter(
    # assigned_to='JP').values()
    # .objects.filter(name__startswith='Beatles').values()
    myTasks = TaskModel.objects.filter(status=True)

    # myTasks = TaskModel.objects.filter(
    # assigned_to__user__first_name='Jwall').values()
    createdTasks = TaskModel.objects.extra(where=["creator_name='JP'"])

    return render(request, "task/task.html", {
        "name": "taskView",
        'taskList': taskList,
        'createdTaskList': createdTasks,
        'myTaskList': myTasks
    })


def modal1(request):
    now = datetime.datetime.now()
    html = "<h1>It is now %s.</h1>" % now
    return HttpResponse(html)
    # return render(request, "task/notifications.html", {
    #     "name": "notifications",
    #     "title": "notifications1",
    # })


def feedback(request):
    return render(request, "feedback/feedback.html", {
        "name": "feedbackView",
    })
