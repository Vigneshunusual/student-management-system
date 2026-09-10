from django.contrib.auth.models import User, Group
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Department


class DepartmentPermissionTestCase(APITestCase):

    def setUp(self):
        self.student = User.objects.create_user(
            username='student',
            password='testpass123'
        )

        self.student_group = Group.objects.create(
            name='Student'
        )

        self.student.groups.add(self.student_group)

        self.department = Department.objects.create(
            name='Computer Science',
            code='CSE'
        )

    def test_student_can_read_department(self):
        self.client.force_authenticate(user=self.student)

        response = self.client.get('/api/departments/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_student_cannot_create_department(self):
        self.client.force_authenticate(user=self.student)

        response = self.client.post(
            '/api/departments/',
            {
                'name': 'Information Technology',
                'code': 'IT'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )


    