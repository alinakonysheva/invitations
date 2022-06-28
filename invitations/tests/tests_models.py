from django.test import TestCase
from invitations.models import Guest, Group, Event, Template

C_GROUP_NAME = 'class'
C_FIRST_NAME = 'John'
C_LAST_NAME = 'Smith'
C_PARENT_NAME = 'Jane'
parent_name = models.CharField(max_length=200, default='Unknown')
parent_phone = models.CharField(max_length=200, default='Unknown')
email = models.EmailField(help_text="jaan@mail.com", default='Unknown')
phone = models.CharField(max_length=200, default='Unknown')
address = models.CharField(max_length=200, default='Unknown')


class TestModels(TestCase):

    def setUp(self):
        self.group1 = Group.objects.create(name=C_GROUP_NAME)
        self.guest1 = Guest.objects.create(group=self.group1, first_name=C_FIRST_NAME, last_name=C_LAST_NAME, parent_name=C_PARENT_NAME)
        self.template1 = Template.objects.create()
        self.event1 = Event.objects.create()
