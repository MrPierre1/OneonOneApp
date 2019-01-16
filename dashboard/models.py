from django.db import models
from django.template.defaultfilters import default
from django.utils import timezone

MANAGER_CHOICES = (
    ('Jean Pierre-Louis', 'JP'),
    ('jack', 'Jack'),
    ('jason', 'Jason')
)


class UserModel(models.Model):
    manager = models.CharField(
        max_length=120, choices=MANAGER_CHOICES, default='JP')
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=15)
    email = models.EmailField()
    photo = models.ImageField(
        upload_to='images/', default='../oneOnOne/static/images/android-desktop.png')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.first_name


class TaskModel(models.Model):
    task = models.CharField(max_length=220)
    creator_name = models.CharField(max_length=30)
    assigned_to = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    due_date = models.DateField(
        auto_now=False, auto_now_add=False, default=timezone.now)
    status = models.BooleanField(default=True)

    # image = models.ImageField()
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.task


class FeedbackModel(models.Model):
    requester_name = models.CharField(max_length=30)
    assigned_to = models.ManyToManyField(UserModel)
    feedback = models.CharField(max_length=220)
    due_date = models.DateField(
        auto_now=False, auto_now_add=False, default=timezone.now)

    # image = models.ImageField()
    class Meta:
        verbose_name = 'Feedback'

    def __str__(self):
        return self.feedback


