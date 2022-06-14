from django.contrib import admin
from .models import Guest, Group, Template, Event
admin.site.register(Guest)
admin.site.register(Group)
admin.site.register(Template)
admin.site.register(Event)