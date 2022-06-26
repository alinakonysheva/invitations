from django.test import SimpleTestCase
from django.urls import resolve, reverse
from invitations.views import *


class TestUrls(SimpleTestCase):

    def test_groups_url_resolves(self):
        url = reverse("groups")
        self.assertEquals(resolve(url).func, groups)

    def test_create_groups_url_resolves(self):
        url = reverse("create_groups")
        self.assertEquals(resolve(url).func, create_groups)

    def test_events_url_resolves(self):
        url = reverse("events")
        self.assertEquals(resolve(url).func, events)

    def test_templates_url_resolves(self):
        url = reverse("templates")
        self.assertEquals(resolve(url).func, templates)

    def test_guests_url_resolves(self):
        url = reverse("guests")
        self.assertEquals(resolve(url).func, guests)

    def test_add_event_url_resolves(self):
        url = reverse("add_event")
        self.assertEquals(resolve(url).func, add_event)

    def test_delete_event_url_resolves(self):
        url = reverse("delete_event")
        self.assertEquals(resolve(url).func, delete_event)

    def test_delete_group_url_resolves(self):
        url = reverse("delete_group")
        self.assertEquals(resolve(url).func, delete_group)

    def test_add_guest_url_resolves(self):
        url = reverse("add_guest")
        self.assertEquals(resolve(url).func, add_guest)

    def test_delete_guest_url_resolves(self):
        url = reverse("delete_guest")
        self.assertEquals(resolve(url).func, delete_guest)

    def test_add_template_url_resolves(self):
        url = reverse("add_template")
        self.assertEquals(resolve(url).func, add_template)

    def test_delete_template_url_resolves(self):
        url = reverse("delete_template")
        self.assertEquals(resolve(url).func, delete_template)

    def test_change_event_url_resolves(self):
        url = reverse("change_event", args=['1'])
        self.assertEquals(resolve(url).func, change_event)

    def test_change_guest_url_resolves(self):
        url = reverse("change_guest", args=['1'])
        self.assertEquals(resolve(url).func, change_guest)

    def test_change_template_url_resolves(self):
        url = reverse("change_template", args=['1'])
        self.assertEquals(resolve(url).func, change_template)

    def test_render_event_url_resolves(self):
        url = reverse("render_event", args=['1'])
        self.assertEquals(resolve(url).func, render_event)

    def test_view_group_url_resolves(self):
        url = reverse("view_group", args=['1'])
        self.assertEquals(resolve(url).func, view_group)