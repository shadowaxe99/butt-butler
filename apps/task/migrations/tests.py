
import unittest
from django.test import TestCase
from apps.task.models import Task

class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Task.objects.create(title='Test Task', description='Test Task Description')

    def test_title_content(self):
        task = Task.objects.get(id=1)
        expected_object_name = f'{task.title}'
        self.assertEquals(expected_object_name, 'Test Task')

    def test_description_content(self):
        task = Task.objects.get(id=1)
        expected_object_description = f'{task.description}'
        self.assertEquals(expected_object_description, 'Test Task Description')

if __name__ == '__main__':
    unittest.main()
