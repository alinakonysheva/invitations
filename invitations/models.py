from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=200)
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="group", null=True)

    def __str__(self):
        return self.name
# итерироваться по группам надо будет так for group in user.group.all

class Guest(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Template(models.Model):
    name = models.CharField(max_length=200)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Event(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event", null=True)

    def __str__(self):
        return self.name
