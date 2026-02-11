from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

# Create your tests here.
class UserAuthTests(TestCase):
    #Test the User registration and Authentication flow

    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('users:register')
        self.token_url = reverse('users:token_obtain_pair')
        self.user_data = {
            'email': 'test@example.com',
            'password': 'password123',
            'name': 'TestUser'
        }

    def test_create_user_success(self):
        #Test creating a user via the API is successful
        response = self.client.post(self.register_url, self.user_data)

        #Checks for status 201 - user was created successfully
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        #verifies user exists in the database
        user_exists = get_user_model().objects.filter(email=self.user_data['email']).exists()
        self.assertTrue(user_exists)

    def test_obtain_token_success(self):
        #Tests that a user can get a JWT token with valid credentials
        #First, create the user
        get_user_model().objects.create_user(
            email=self.user_data['email'],
            password=self.user_data['password'],
        )

        #Now, attempt to obtain a token
        payload = {
            'email': self.user_data['email'],
            'password': self.user_data['password']
        }
        response = self.client.post(self.token_url, payload)

        #checks if the response contains the access and refresh keys
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_token_with_wrong_password(self):
        #Tests that a token is NOT isssued with a wrong passord
        get_user_model().objects.create_user(
            email=self.user_data['email'],
            password=self.user_data['password'],
        )
        payload = {
            'email': self.user_data['email'],
            'password': 'wrongpassword'
        } 
        response = self.client.post(self.token_url, payload)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)