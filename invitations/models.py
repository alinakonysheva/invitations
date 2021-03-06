import datetime

from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Group(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="group", null=True)

    def __str__(self):
        return self.name


class Guest(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    parent_name = models.CharField(max_length=200, default='Unknown')
    parent_phone = models.CharField(max_length=200, default='Unknown')
    email = models.EmailField(help_text="jaan@mail.com", default='Unknown')
    phone = models.CharField(max_length=200, default='Unknown')
    address = models.CharField(max_length=200, default='Unknown')

    def __str__(self):
        return self.first_name


class Template(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField(max_length=500)
    template_file = models.TextField(max_length=500)
    example_img = models.TextField(max_length=500)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="template", null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    host = models.CharField(max_length=100)
    date = models.DateField(default=date.today())
    start = models.TimeField(default=datetime.time(16, 00))
    finish = models.TimeField(default=datetime.time(16, 00))
    place = models.CharField(max_length=200)
    contact_number = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event", null=True)

    def __str__(self):
        return self.name
