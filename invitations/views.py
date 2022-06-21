import datetime

from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from .models import Group, Guest, Event, Template
from .forms import NewGroupForm, AddEventForm, DeleteForm, AddGuestForm, AddTemplateForm


def index(response, id):
    group = Group.objects.get(id=id)
    guest_1 = group.guest_set.get(id=1)
    return render(response, "invitations/base.html", {"group_name": group.name, "guest_name": guest_1.name})


def home(response):
    return render(response, "invitations/home.html")


def groups(response):
    groups_ = Group.objects.all()
    return render(response, "invitations/groups.html", {"groups": groups_})


def create_groups(response):
    if response.method == "POST":
        form = NewGroupForm(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            g = Group(name=n)
            g.save()
            groups_ = Group.objects.all()
            return render(response, "invitations/groups.html", {"groups": groups_})

    else:
        groups_ = Group.objects.all()
        return render(response, "invitations/create_groups.html", {"groups": groups_})


def delete_group(response):
    if response.method == "POST":
        form = DeleteForm(response.POST)
        if form.is_valid():
            group_id = form.cleaned_data["id"]
            try:
                group = Group.objects.get(id=group_id)
                if group:
                    group.delete()
                    groups_ = Group.objects.all()
                    return render(response, "invitations/groups.html", {"groups": groups_})
            except Exception as e:
                groups_ = Group.objects.all()
                return render(response, "invitations/groups.html", {"groups": groups_})
        else:
            groups_ = Group.objects.all()
            return render(response, "invitations/groups.html", {"groups": groups_})


def events(response):
    events_ = Event.objects.all()
    return render(response, "invitations/events.html", {"events": events_})


def add_event(response):
    if response.method == "POST":
        form = AddEventForm(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            g = int(form.cleaned_data["group"])
            t = int(form.cleaned_data["template"])
            e = Event(name=n, group_id=g, template_id=t)
            e.save()
            events_ = Event.objects.all()
            return render(response, "invitations/events.html", {"events": events_})

    else:
        form = AddEventForm(response.POST)
        form.is_valid()
        return render(response, "invitations/add_event.html", {"form": form})


def delete_event(response):
    if response.method == "POST":
        form = DeleteForm(response.POST)
        if form.is_valid():
            event_id = form.cleaned_data["id"]
            try:
                event = Event.objects.get(id=event_id)
                if event:
                    event.delete()
                    events_ = Event.objects.all()
                    return render(response, "invitations/events.html", {"events": events_})
            except Exception as e:
                events_ = Event.objects.all()
                return render(response, "invitations/events.html", {"events": events_})
        else:
            events_ = Event.objects.all()
            return render(response, "invitations/events.html", {"events": events_})


def templates(response):
    templates_ = Template.objects.all()
    return render(response, "invitations/templates.html", {"templates": templates_})


def guests(response):
    groups_ = Group.objects.all()
    return render(response, "invitations/guests.html", {"groups": groups_})


def add_guest(response):
    if response.method == "POST":
        form = AddGuestForm(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            g = form.cleaned_data["group"]
            guest = Guest(name=n, group=g)
            guest.save()
            groups_ = Group.objects.all()
            return render(response, "invitations/guests.html", {"groups": groups_})
    else:
        form = AddGuestForm(response.POST)
        return render(response, "invitations/add_guest.html", {"form": form})


def change_guest(response, guest_id):
    if response.method == "POST":
        form = AddGuestForm(response.POST)
        form.is_valid()
        guest = Guest.objects.select_for_update().get(id=guest_id)
        guest.name = form.instance.name
        guest.group = form.instance.group
        guest.save()
        return redirect("/guests/")
    else:
        guest = Guest.objects.get(id=guest_id)
        form = AddGuestForm(instance=guest)
        return render(response, "invitations/change_guest.html", {"form": form})


def delete_guest(response):
    if response.method == "POST":
        form = DeleteForm(response.POST)
        if form.is_valid():
            guest_id = form.cleaned_data["id"]
            try:
                guest = Guest.objects.get(id=guest_id)
                if guest:
                    guest.delete()
                    return redirect("/guests/")
            except Exception as e:
                return redirect("/guests/")
        else:
            return redirect("/guests/")


def add_template(response):
    if response.method == "POST":
        form = AddTemplateForm(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            c = form.cleaned_data["content"]
            template_ = Template(name=n, content=c)
            template_.save()
            return redirect("/templates/")
    else:
        form = AddTemplateForm(response.POST)
        return render(response, "invitations/add_template.html", {"form": form})


def change_template(response, template_id):
    if response.method == "POST":
        form = AddTemplateForm(response.POST)
        form.is_valid()
        template = Template.objects.select_for_update().get(id=template_id)
        template.name = form.instance.name
        template.content = form.instance.content
        template.save()
        return redirect("/templates/")
    else:
        template = Template.objects.get(id=template_id)
        form = AddTemplateForm(instance=template)
        return render(response, "invitations/change_template.html", {"form": form})


def delete_template(response):
    if response.method == "POST":
        form = DeleteForm(response.POST)
        if form.is_valid():
            template_id = form.cleaned_data["id"]
            try:
                template = Template.objects.get(id=template_id)
                if template:
                    template.delete()
                    return redirect("/templates/")
            except Exception as e:
                return redirect("/templates/")
        else:
            return redirect("/templates/")


def render_event(response, event_id):
    event = Event.objects.get(id=event_id)
    rendered_content_list = map(lambda g: render_event_for_guest(event, g),
                                event.group.guest_set.all())
    return render(response, "invitations/render_template.html",
                  {"event_name": event.name, "content_strings": rendered_content_list})


def render_event_for_guest(event, guest):
    render_content = event.template.content.replace("_GUEST_NAME_", guest.name) \
        .replace("_DATE_", str(datetime.date.today()))
    return render_content
