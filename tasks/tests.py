from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task

class TaskPermissionTests(TestCase):
    """Test permissions and error handling for Tasks"""

    def setUp(self):
        self.client = APIClient()
        self.user_a = get_user_model().objects.create_user(
            email='user_a@example.com', password='password123', name='User A'
        )
        self.user_b = get_user_model().objects.create_user(
            email='user_b@example.com', password='password123', name='User B'
        )
        self.task_a = Task.objects.create(
            user=self.user_a, 
            title='User A Task', 
            description='Private info'
        )
        self.list_url = reverse('task-list')
        # detail_url looks like /api/tasks/1/
        self.detail_url = reverse('task-detail', kwargs={'pk': self.task_a.id})

    def test_user_can_only_see_their_own_tasks(self):
        """Test that the task list only returns tasks owned by the user"""
        self.client.force_authenticate(user=self.user_b)
        response = self.client.get(self.list_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # User B has 0 tasks, so the list should be empty even though Task A exists
        self.assertEqual(len(response.data), 0)

    def test_forbidden_to_access_other_user_task(self):
        """Test that accessing another user's task results in 404 or 403"""
        self.client.force_authenticate(user=self.user_b)
        response = self.client.get(self.detail_url)
        
        # Because of our 'get_queryset' filter, User B can't even "see" Task A exists.
        # So Django returns 404 Not Found.
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_custom_error_format(self):
        """Test that our custom error handler is working"""
        self.client.force_authenticate(user=self.user_b)
        response = self.client.get(self.detail_url)
        
        # Check if the error matches our custom { 'error': '...', 'status_code': ... } format
        self.assertIn('error', response.data)
        self.assertEqual(response.data['status_code'], 404)

    def test_toggle_task_ownership(self):
        """Test that User B cannot toggle User A's task"""
        toggle_url = reverse('task-toggle', kwargs={'pk': self.task_a.id})
        self.client.force_authenticate(user=self.user_b)
        response = self.client.post(toggle_url)
        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # Ensure the task status didn't change
        self.task_a.refresh_from_db()
        self.assertFalse(self.task_a.is_completed)