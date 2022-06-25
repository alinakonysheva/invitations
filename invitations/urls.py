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
               path(f"guests/add/", views.add_guest, name="add_guest"),
               path(f"guests/change/<int:guest_id>", views.change_guest, name="change_guest"),
               path(f"guests/delete/", views.delete_guest, name="delete_guest"),
               path(f"templates/add/", views.add_template, name="add_template"),
               path(f"templates/change/<int:template_id>", views.change_template, name="change_template"),
               path(f"templates/delete/", views.delete_template, name="delete_template"),
               path(f"events/render/<int:event_id>", views.render_event, name="render_event"),
               path(f"groups/view_group/<int:group_id>", views.view_group, name="view_group"),

               ]
