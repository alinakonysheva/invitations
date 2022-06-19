from django import forms
from .models import Group, Template

existing_groups = Group.objects.all()
tuples_existing_groups = tuple([(group.id, group.name) for group in existing_groups])
existing_templates = Template.objects.all()
tuples_existing_templates = tuple([(template.id, template.name) for template in existing_templates])


class NewGroupForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200)


class AddEventForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    group = forms.ChoiceField(label="Group", choices=tuples_existing_groups)
    template = forms.ChoiceField(label="Template", choices=tuples_existing_templates)


class DeleteForm(forms.Form):
    id = forms.IntegerField(label="id")


class AddGuestForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    group = forms.ChoiceField(label="Group", choices=tuples_existing_groups)
