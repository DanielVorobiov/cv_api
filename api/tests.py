from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from common.cv_data import cv_data


class CurriculumVitaeTestCase(APITestCase):

    def test_get_about(self):
        response = self.client.get('/api/about/')
        self.assertEqual(response.data['value'], cv_data['about'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_experience(self):
        response = self.client.get('/api/experience/')
        self.assertEqual(response.data['value'], cv_data['experience'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_education(self):
        response = self.client.get('/api/education/')
        self.assertEqual(response.data['value'], cv_data['education'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_volunteering(self):
        response = self.client.get('/api/volunteering/')
        self.assertEqual(response.data['value'], cv_data['volunteering'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_contacts(self):
        response = self.client.get('/api/contacts/')
        self.assertEqual(response.data['value'], cv_data['contacts'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_soft_skills(self):
        response = self.client.get('/api/soft-skills/')
        self.assertEqual(response.data['value'], cv_data['soft-skills'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_technical_skills(self):
        response = self.client.get('/api/technical-skills/')
        self.assertEqual(response.data['value'], cv_data['technical-skills'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_languages(self):
        response = self.client.get('/api/languages/')
        self.assertEqual(response.data['value'], cv_data['languages'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_awards(self):
        response = self.client.get('/api/awards/')
        self.assertEqual(response.data['value'], cv_data['awards'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_hobbies(self):
        response = self.client.get('/api/hobbies/')
        self.assertEqual(response.data['value'], cv_data['hobbies'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
