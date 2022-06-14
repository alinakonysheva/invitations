from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Group, Guest, Event, Template
from .forms import NewGroupForm


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
        new_form = NewGroupForm()
        return render(response, "invitations/create_groups.html", {"form": new_form})


def events(response):
    events_ = Event.objects.all()
    return render(response, "invitations/events.html", {"events": events_})


def templates(response):
    templates_ = Template.objects.all()
    return render(response, "invitations/templates.html", {"templates": templates_})


def guests(response):
    groups_ = Group.objects.all()
    return render(response, "invitations/guests.html", {"groups": groups_})
