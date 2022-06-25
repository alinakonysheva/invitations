from django import forms
from django.forms import NumberInput, DateInput, TimeInput

from .models import Group, Template, Guest, Event


def get_tuples_groups():
    return tuple([(group.id, group.name) for group in Group.objects.all()])


class NewGroupForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200)


def get_tuples_templates():
    return tuple([(template.id, template.name) for template in Template.objects.all()])


class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['group', 'template', 'name', 'host', 'date', 'start', 'finish', 'place', 'contact_number',
                  'contact_person']
        widgets = {'date': DateInput(attrs={'type': 'date'}),
                   'start': TimeInput(attrs={'type': 'time'}),
                   'finish': TimeInput(attrs={'type': 'time'}),
                   'user': forms.HiddenInput()}


class DeleteForm(forms.Form):
    id = forms.IntegerField(label="id")


class AddGuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = '__all__'


class AddTemplateForm(forms.ModelForm):
    class Meta:
        model = Template
        fields = ['name', 'content']
