import datetime

from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import time
from datetime import date

from .models import Group, Guest, Event, Template
from .forms import NewGroupForm, AddEventForm, DeleteForm, AddGuestForm, AddTemplateForm


def index(request, id):
    group = Group.objects.get(id=id)
    guest_1 = group.guest_set.get(id=1)
    return render(request, "invitations/base.html", {"group_name": group.name, "guest_name": guest_1.name})


def home(request):
    return render(request, "invitations/home.html")

# TODO: redirect to login page if not authen

# TODO: view group: name, list guests
# TODO: event grouplink - group view
# TODO logout
def groups(request):
    user = request.user
    groups_ = user.group.all
    return render(request, "invitations/groups.html", {"groups": groups_})


def create_groups(request):
    if request.method == "POST":
        form = NewGroupForm(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            g = Group(name=n)
            g.save()
            groups_ = Group.objects.all()
            return render(request, "invitations/groups.html", {"groups": groups_})

    else:
        groups_ = Group.objects.all()
        return render(request, "invitations/create_groups.html", {"groups": groups_})


def delete_group(request):
    if request.method == "POST":
        form = DeleteForm(request.POST)
        if form.is_valid():
            group_id = form.cleaned_data["id"]
            try:
                group = Group.objects.get(id=group_id)
                if group:
                    group.delete()
                    groups_ = Group.objects.all()
                    return render(request, "invitations/groups.html", {"groups": groups_})
            except Exception as e:
                groups_ = Group.objects.all()
                return render(request, "invitations/groups.html", {"groups": groups_})
        else:
            groups_ = Group.objects.all()
            return render(request, "invitations/groups.html", {"groups": groups_})


def events(request):
    events_ = Event.objects.all()
    return render(request, "invitations/events.html", {"events": events_})


def add_event(request):
    if request.method == "POST":
        form = AddEventForm(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            g = form.cleaned_data["group"]
            t = form.cleaned_data["template"]
            h = form.cleaned_data["host"]
            d = str(form.cleaned_data["date"])
            st = str(form.cleaned_data["start"])
            fin = str(form.cleaned_data["finish"])
            pl = form.cleaned_data["place"]
            cn = form.cleaned_data["contact_number"]
            cp = form.cleaned_data["contact_person"]
            e = Event(name=n, group_id=g.id, template_id=t.id, host=h, place=pl,
                      contact_number=cn, contact_person=cp, date=d, start=st, finish=fin)
            e.save()
            events_ = Event.objects.all()
            return render(request, "invitations/events.html", {"events": events_})

    else:
        form = AddEventForm(request.POST)
        form.is_valid()
        return render(request, "invitations/add_event.html", {"form": form})


def delete_event(request):
    if request.method == "POST":
        form = DeleteForm(request.POST)
        if form.is_valid():
            event_id = form.cleaned_data["id"]
            try:
                event = Event.objects.get(id=event_id)
                if event:
                    event.delete()
                    events_ = Event.objects.all()
                    return render(request, "invitations/events.html", {"events": events_})
            except Exception as e:
                events_ = Event.objects.all()
                return render(request, "invitations/events.html", {"events": events_})
        else:
            events_ = Event.objects.all()
            return render(request, "invitations/events.html", {"events": events_})


def templates(request):
    templates_ = Template.objects.all()
    return render(request, "invitations/templates.html", {"templates": templates_})


def guests(request):
    groups_ = Group.objects.all()
    return render(request, "invitations/guests.html", {"groups": groups_})


def add_guest(request):
    if request.method == "POST":
        form = AddGuestForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data["first_name"]
            g = form.cleaned_data["group"]
            ln = form.cleaned_data["last_name"]
            pn = form.cleaned_data["parent_name"]
            p_ph = form.cleaned_data["parent_phone"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            address = form.cleaned_data["address"]

            guest = Guest(first_name=n, group=g, last_name=ln, parent_name=pn, parent_phone=p_ph,
                          email=email, phone=phone, address=address)
            guest.save()
            groups_ = Group.objects.all()
            return render(request, "invitations/guests.html", {"groups": groups_})
    else:
        form = AddGuestForm(request.POST)
        return render(request, "invitations/add_guest.html", {"form": form})


def change_guest(request, guest_id):
    if request.method == "POST":
        form = AddGuestForm(request.POST)
        form.is_valid()
        guest = Guest.objects.select_for_update().get(id=guest_id)
        guest.first_name = form.instance.first_name
        guest.last_name = form.instance.last_name
        guest.parent_name = form.instance.parent_name
        guest.parent_phone = form.instance.parent_phone
        guest.email = form.instance.email
        guest.phone = form.instance.phone
        guest.address = form.instance.address
        guest.group = form.instance.group
        guest.save()
        return redirect("/guests/")
    else:
        guest = Guest.objects.get(id=guest_id)
        form = AddGuestForm(instance=guest)
        return render(request, "invitations/change_guest.html", {"form": form})


def delete_guest(request):
    if request.method == "POST":
        form = DeleteForm(request.POST)
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


def add_template(request):
    if request.method == "POST":
        form = AddTemplateForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            c = form.cleaned_data["content"]
            template_ = Template(name=n, content=c)
            template_.save()
            return redirect("/templates/")
    else:
        form = AddTemplateForm(request.POST)
        return render(request, "invitations/add_template.html", {"form": form})


def change_template(request, template_id):
    if request.method == "POST":
        form = AddTemplateForm(request.POST)
        form.is_valid()
        template = Template.objects.select_for_update().get(id=template_id)
        template.name = form.instance.name
        template.content = form.instance.content
        template.save()
        return redirect("/templates/")
    else:
        template = Template.objects.get(id=template_id)
        form = AddTemplateForm(instance=template)
        return render(request, "invitations/change_template.html", {"form": form})


def delete_template(request):
    if request.method == "POST":
        form = DeleteForm(request.POST)
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


def render_event(request, event_id):
    event = Event.objects.get(id=event_id)
    rendered_content_list = map(lambda g: render_event_for_guest(event, g),
                                event.group.guest_set.all())
    return render(request, "invitations/render_template.html",
                  {"event_name": event.name, "content_strings": rendered_content_list})


def render_event_for_guest(event, guest):
    render_content = event.template.content.replace("_GUEST_NAME_", guest.first_name) \
        .replace("_DATE_", str(datetime.date.today()))
    return render_content
