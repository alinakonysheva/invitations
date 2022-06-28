from django.test import TestCase
from invitations.models import Guest, Group, Event, Template
from datetime import date
import datetime

C_GROUP_NAME = 'class'
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


class TestModels(TestCase):

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

    def test_group(self):
        self.assertEquals(self.group1.name, C_GROUP_NAME)

    def test_group_all_guests(self):
        self.assertEquals(len(self.group1.guest_set.all()), 1)

    def test_guest(self):
        self.assertEquals(self.guest1.group.id, self.group1.id)
        self.assertEquals(self.guest1.first_name, C_FIRST_NAME)
        self.assertEquals(self.guest1.last_name, C_LAST_NAME)
        self.assertEquals(self.guest1.parent_name, C_PARENT_NAME)
        self.assertEquals(self.guest1.parent_phone, C_PARENT_PHONE)
        self.assertEquals(self.guest1.email, C_EMAIL)
        self.assertEquals(self.guest1.phone, C_PHONE)
        self.assertEquals(self.guest1.address, C_ADDRESS)

    def test_template(self):
        self.assertEquals(self.template1.name, C_TEMPLATE_NAME)
        self.assertEquals(self.template1.content, C_CONTENT)
        self.assertEquals(self.template1.template_file, C_TEMPLATE_FILE)
        self.assertEquals(self.template1.example_img, C_EXAMPLE_IMG)

    def test_event(self):
        self.assertEquals(self.event1.name, C_EVENT_NAME)
        self.assertEquals(self.event1.host, C_HOST)
        self.assertEquals(self.event1.date, C_DATE)
        self.assertEquals(self.event1.start, C_TIME_START)
        self.assertEquals(self.event1.finish, C_TIME_FINISH)
        self.assertEquals(self.event1.place, C_PLACE)
        self.assertEquals(self.event1.contact_number, C_CONTACT_NUMBER)
        self.assertEquals(self.event1.contact_person, C_CONTACT_PERSON)

    def test_event_template(self):
        self.assertEquals(self.event1.group.id, self.group1.id)

    def test_event_group(self):
        self.assertEquals(self.event1.template.id, self.template1.id)



