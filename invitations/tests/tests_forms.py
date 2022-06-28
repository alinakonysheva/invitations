from django.test import TestCase
from datetime import date
import datetime
from invitations.forms import NewGroupForm, AddEventForm, AddGuestForm, AddTemplateForm
from invitations.models import Guest, Group, Event, Template

C_GROUP_NAME = 'class'
C_INCORRECT_NAME = 'spam' * 75
C_FIRST_NAME = 'John'
C_LAST_NAME = 'Smith'
C_PARENT_NAME = 'Jane'
C_PARENT_PHONE = '0485672345'
C_EMAIL = "jaan@mail.com"
C_PHONE = '0485672345'
C_ADDRESS = 'Bevel, Bevel-Dorp 125'

C_TEMPLATE_NAME = 'birthday'
C_CONTENT = 'Happy birthday'
C_TEMPLATE_FILE = 'file'
C_EXAMPLE_IMG = 'img'

C_EVENT_NAME = 'Lev is 10!'
C_HOST = 'Lev'
C_DATE = date.today()
C_TIME_START = datetime.time(16, 00)
C_TIME_FINISH = datetime.time(18, 00)
C_PLACE = 'De Kloek'
C_CONTACT_NUMBER = '04542318345'
C_CONTACT_PERSON = 'mama An'


class TestForms(TestCase):
    def setUp(self):
        self.group1 = Group.objects.create(name=C_GROUP_NAME)
        self.guest1 = Guest.objects.create(group=self.group1, first_name=C_FIRST_NAME, last_name=C_LAST_NAME,
                                           parent_name=C_PARENT_NAME, parent_phone=C_PARENT_PHONE, email=C_EMAIL,
                                           phone=C_PHONE, address=C_ADDRESS)
        self.template1 = Template.objects.create(name=C_TEMPLATE_NAME, content=C_CONTENT, template_file=C_TEMPLATE_FILE,
                                                 example_img=C_EXAMPLE_IMG)
        self.event1 = Event.objects.create(group=self.group1, template=self.template1, name=C_EVENT_NAME, host=C_HOST,
                                           date=C_DATE, start=C_TIME_START, finish=C_TIME_FINISH, place=C_PLACE,
                                           contact_number=C_CONTACT_NUMBER, contact_person=C_CONTACT_PERSON)

    def test_new_group_form(self):
        form = NewGroupForm(data={'name': C_GROUP_NAME})
        self.assertTrue(form.is_valid())

    def test_new_group_form_long_name(self):
        form = NewGroupForm(data={'name': C_INCORRECT_NAME})
        self.assertFalse(form.is_valid())

    def test_new_group_form_no_name(self):
        form = NewGroupForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_new_template_form(self):
        form = AddTemplateForm(data={'name': C_TEMPLATE_NAME,
                                     'content': C_CONTENT,
                                     'template_file': C_TEMPLATE_FILE,
                                     'example_img': C_EXAMPLE_IMG})
        self.assertTrue(form.is_valid())

    def test_new_template_form_no_data(self):
        form = AddTemplateForm(data={})
        self.assertFalse(form.is_valid())

    def test_new_template_form_long_name(self):
        form = AddTemplateForm(data={'name': C_INCORRECT_NAME,
                                     'content': C_CONTENT,
                                     'template_file': C_TEMPLATE_FILE,
                                     'example_img': C_EXAMPLE_IMG})
        self.assertFalse(form.is_valid())

    def test_new_guest_form(self):
        group_all = Group.objects.all()
        groups = list(map(lambda group_: (group_.id, group_.name), group_all))
        form = AddGuestForm(groups=groups, data={'group': 1,
                                                 'first_name': C_FIRST_NAME,
                                                 'last_name': C_LAST_NAME,
                                                 'parent_name': C_PARENT_NAME,
                                                 'parent_phone': C_PARENT_PHONE,
                                                 'email': C_EMAIL,
                                                 'phone': C_PHONE,
                                                 'address': C_ADDRESS})
        self.assertTrue(form.is_valid())

    def test_new_guest_form_long_name(self):
        group_all = Group.objects.all()
        groups = list(map(lambda group_: (group_.id, group_.name), group_all))
        form = AddGuestForm(groups=groups, data={'group': 1,
                                                 'first_name': C_INCORRECT_NAME,
                                                 'last_name': C_LAST_NAME,
                                                 'parent_name': C_PARENT_NAME,
                                                 'parent_phone': C_PARENT_PHONE,
                                                 'email': C_EMAIL,
                                                 'phone': C_PHONE,
                                                 'address': C_ADDRESS})
        self.assertFalse(form.is_valid())

    def test_new_guest_form_no_data(self):
        group_all = Group.objects.all()
        groups = list(map(lambda group_: (group_.id, group_.name), group_all))
        form = AddGuestForm(groups=groups, data={})
        self.assertFalse(form.is_valid())
