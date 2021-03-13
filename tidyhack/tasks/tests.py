from django.http import response
from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client




# Create your tests here.
class HomePageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        expectedResponseStatusCode = 200
        self.assertEqual(response.status_code,expectedResponseStatusCode)


    def test_home_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)


    def test_home_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')




class AboutPageTests(SimpleTestCase):
    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        expectedResponseStatusCode = 200
        self.assertEqual(response.status_code,expectedResponseStatusCode)

    
    def test_about_view_url_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code,200)


    def test_about_view_uses_correct_template(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')




class ScrapbookFormPageTests(TestCase):

    def setUp(self):
        # Create two users
        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(username='testuser2', password='2HJ1vRV0Z&3iD')

        test_user1.save()
        test_user2.save()


    def test_scrapbookform_page_redirect(self):
        response = self.client.get('/scrapbook/enterDate/')
        expectedResponseStatusCode = 302
        self.assertEqual(response.status_code,expectedResponseStatusCode)


    def test_scrapbookform_view_url_by_name_redirect(self):
        response = self.client.get(reverse('scrapbookdate'))
        self.assertEqual(response.status_code,302)


    def test_scrapbookform_page_status_code(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get('/scrapbook/enterDate/')
        expectedResponseStatusCode = 200
        self.assertEqual(response.status_code,expectedResponseStatusCode)

    
    def test_scrapbookform_view_url_by_name(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('scrapbookdate'))
        self.assertEqual(response.status_code,200)


    def test_scrapbookform_view_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('scrapbookdate'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/scrapbookForm.html')