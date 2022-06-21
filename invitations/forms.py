from django import forms

from .models import Group, Template, Guest


def get_tuples_groups():
    return tuple([(group.id, group.name) for group in Group.objects.all()])


class NewGroupForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200)


def get_tuples_templates():
    return tuple([(template.id, template.name) for template in Template.objects.all()])


class AddEventForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    group = forms.ChoiceField(label="Group", choices=get_tuples_groups())
    template = forms.ChoiceField(label="Template", choices=get_tuples_templates())
    host = forms.CharField(label="Host", max_length=200)


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
