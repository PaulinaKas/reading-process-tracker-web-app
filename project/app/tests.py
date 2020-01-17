from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from app.views import homePage

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_saves_POST_request(self):
        response = self.client.post('/', data={'title': 'Some book\'s title'})
        self.assertIn('Some book\'s title', response.content.decode())
