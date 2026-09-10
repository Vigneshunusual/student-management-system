from django.contrib.auth.models import User, Group
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Student
from departments.models import Department


class StudentPermissionTestCase(APITestCase):

    def setUp(self):
        self.student_group = Group.objects.create(
            name='Student'
        )

        self.department = Department.objects.create(
            name='Computer Science',
            code='CSE'
        )

        self.user1 = User.objects.create_user(
            username='student1',
            password='testpass123'
        )
        self.user1.groups.add(self.student_group)

        self.user2 = User.objects.create_user(
            username='student2',
            password='testpass123'
        )
        self.user2.groups.add(self.student_group)

        self.student1 = Student.objects.create(
            user=self.user1,
            student_id='STU001',
            department=self.department,
            date_of_birth='2002-01-01',
            phone='9876543210',
            address='Chennai',
            enrollment_date='2026-06-01'
        )

        self.student2 = Student.objects.create(
            user=self.user2,
            student_id='STU002',
            department=self.department,
            date_of_birth='2002-02-02',
            phone='9876543211',
            address='Chennai',
            enrollment_date='2026-06-01'
        )

    def test_student_can_access_own_record(self):
        self.client.force_authenticate(user=self.user1)

        response = self.client.get(
            f'/api/students/{self.student1.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_student_cannot_access_other_student(self):
        self.client.force_authenticate(user=self.user1)

        response = self.client.get(
            f'/api/students/{self.student2.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )