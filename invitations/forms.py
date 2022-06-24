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
    """    name = forms.CharField(label="Event", max_length=200)
        group = forms.ChoiceField(label="Group", choices=get_tuples_groups())
        template = forms.ChoiceField(label="Template", choices=get_tuples_templates())
        host = forms.CharField(label="Host name", max_length=200)
        date = forms.DateField(label="Event date")
        # start = forms.DateTimeField()
        # finish = forms.DateTimeField()
        place = forms.CharField(max_length=200)
        contact_number = forms.CharField(max_length=100)
        contact_person = forms.CharField(max_length=100)"""

    class Meta:
        model = Event
        fields = '__all__'
        widgets = {'date': DateInput(attrs={'type': 'date'}),
                   'start': TimeInput(attrs={'type': 'time'}),
                   'finish': TimeInput(attrs={'type': 'time'})}


class DeleteForm(forms.Form):
    id = forms.IntegerField(label="id")


class AddGuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = '__all__'


class AddTemplateForm(forms.ModelForm):
    class Meta:
        model = Template
        fields = '__all__'
