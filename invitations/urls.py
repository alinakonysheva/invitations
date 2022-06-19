from django.urls import path
from . import views

urlpatterns = [path(f"<int:id>", views.index, name="index"),
               path(f"home/", views.home, name="home"),
               path(f"", views.home, name="home"),
               path(f"groups/", views.groups, name="groups"),
               path(f"groups/add", views.create_groups, name="create_groups"),
               path(f"events/", views.events, name="events"),
               path(f"templates/", views.templates, name="templates"),
               path(f"guests/", views.guests, name="guests"),
               path(f"events/add/", views.add_event, name="add_event"),
               path(f"events/delete/", views.delete_event, name="delete_event"),
               path(f"groups/delete/", views.delete_group, name="delete_group"),

               ]
