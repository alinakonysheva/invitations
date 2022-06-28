from django.test import TestCase
from datetime import date
import datetime
from invitations.forms import NewGroupForm, AddEventForm, DeleteForm, AddGuestForm, AddTemplateForm

C_GROUP_NAME = 'class'
C_GROUP_INCORRECT_NAME = 'spam' * 100
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
    def test_new_group_form(self):
        form = NewGroupForm(data={'name': C_GROUP_NAME})
        self.assertTrue(form.is_valid())

    def test_new_group_form_long_name(self):
        form = NewGroupForm(data={'name': C_GROUP_INCORRECT_NAME})
        self.assertFalse(form.is_valid())

    def test_new_group_form_no_name(self):
        form = NewGroupForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

