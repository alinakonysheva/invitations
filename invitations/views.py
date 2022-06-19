from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Group, Guest, Event, Template
from .forms import NewGroupForm, AddEventForm, DeleteForm, AddGuestForm


# Create your views here.

def index(response, id):
    group = Group.objects.get(id=id)
    guest_1 = group.guest_set.get(id=1)
    # return HttpResponse("<h1> %s, %s </h1>" % (group.name, guest_1.name))
    return render(response, "invitations/base.html", {"group_name": group.name, "guest_name": guest_1.name})


def home(response):
    return render(response, "invitations/home.html")


def groups(response):
    groups_ = Group.objects.all()
    return render(response, "invitations/groups.html", {"groups": groups_})


""" if response.method == "POST":
        if response.POST.get("save"):
            for guest in groups_.guest_set.all():
                if response.POST.get("c" + str(guest)) == "clicked":
                    
        elif response.POST.get("save_guest"):
"""


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
            g = int(form.cleaned_data["group"])
            guest = Guest(name=n, group_id=g)
            guest.save()
            groups_ = Group.objects.all()
            return render(response, "invitations/guests.html", {"groups": groups_})

    else:
        form = AddGuestForm(response.POST)
        return render(response, "invitations/add_guest.html", {"form": form})


def change_guest(response):
    pass


def delete_guest(response):
    if response.method == "POST":
        form = DeleteForm(response.POST)
        if form.is_valid():
            guest_id = form.cleaned_data["id"]
            try:
                guest = Guest.objects.get(id=guest_id)
                if guest:
                    guest.delete()
                    groups_ = Group.objects.all()
                    return render(response, "invitations/guests.html", {"groups": groups_})
            except Exception as e:
                groups_ = Group.objects.all()
                return render(response, "invitations/guests.html", {"groups": groups_})
        else:
            groups_ = Group.objects.all()
            return render(response, "invitations/guests.html", {"groups": groups_})