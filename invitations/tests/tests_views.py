from datetime import date, datetime
from django.utils import timezone
import django
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from invitations.views import render_event
import json
from invitations.models import Guest, Group, Template, Event


class TestViews(TestCase):
    c = Client()

    def setUp(self):
        user = User.objects.create(username='TestUser')
        user.set_password('GoolyBooly12345')
        user.save()
        self.client = self.c.login(username='TestUser', password='GoolyBooly12345')
        self.events = reverse('events')
        self.groups = reverse('groups')
        self.templates = reverse('templates')
        self.guests = reverse('guests')
        """self.group = Group(name=1, user=self.client)
        self.guest = Guest(group=self.group, first_name='test', last_name='test', parent_name='test',
                           parent_phone='1', email='12@mail.ru', phone='342', address='address')
        self.template = Template(name='templ', content='templ', template_file='dd', example_img='sdf', user=self.client)
        self.event = Event(group=self.group, template=self.template, name='Birthday', host='Ana', date=date.today(),
                           start=timezone.now(), finish=timezone.now(), place='place11', contact_number='0000',
                           contact_person='mama', user= self.client)
        self.change_guest = reverse('change_guest', args=['1'])"""

    def test_groups_get(self):
        response = self.c.get(self.groups)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'invitations/groups.html')

    def test_events_get(self):
        response = self.c.get(self.events)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'invitations/events.html')

    def test_templates_get(self):
        response = self.c.get(self.templates)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'invitations/templates.html')

    def test_guests_get(self):
        response = self.c.get(self.guests)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'invitations/guests.html')

    """def test_change_guests_get(self):
        response = self.c.get(self.change_guest)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'invitations/change_guest.html')
"""