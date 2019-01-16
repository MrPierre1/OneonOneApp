from django.contrib import admin

# Register your models here.
from .models import UserModel
from .models import TaskModel
from .models import FeedbackModel

admin.site.register(UserModel)
admin.site.register(TaskModel)
admin.site.register(FeedbackModel)
