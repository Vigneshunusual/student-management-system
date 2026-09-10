from django.contrib.auth.models import User, Group
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Course


class CourseAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testadmin',
            password='testpass123'
        )

        self.admin_group = Group.objects.create(
            name='Admin'
        )

        self.user.groups.add(self.admin_group)

        self.course = Course.objects.create(
            name='Python Programming',
            code='PY101',
            credits=4
        )

        self.client.force_authenticate(user=self.user)

    def test_list_courses(self):
        response = self.client.get('/api/courses/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.data['count'],
            1
        )

    def test_invalid_course_credits(self):
        data = {
            'name': 'Invalid Course',
            'code': 'TEST101',
            'credits': 10
        }

        response = self.client.post(
            '/api/courses/',
            data,
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_course_filtering(self):
            response = self.client.get(
            '/api/courses/?credits=4'
        )
    
            self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
    
            self.assertEqual(
            response.data['count'],
            1
        )
    
    
    def test_course_search(self):
        response = self.client.get(
            '/api/courses/?search=Python'
        )
    
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
    
        self.assertEqual(
            response.data['count'],
            1
        )