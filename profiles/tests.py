from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Profile

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save

from rest_framework.test import APIClient

User = get_user_model()

# Create your tests here.

class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="ABC", password="somepassword")
        self.user_v2 = User.objects.create_user(username="ABCD", password="somepassword3")
        
    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='somepassword')
        return client

    def test_profile_created_via_signal(self):
        qs = Profile.objects.all()
        self.assertEqual(qs.count(), 2)

    def test_following(self):
        first = self.user
        second = self.user_v2
        first.profile.followers.add(second)
        second_user_following_whom = second.following.all()
        qs = second_user_following_whom.filter(user=first)
        first_user_following_no_one = first.following.all()
        self.assertTrue(qs.exists())
        self.assertFalse(first_user_following_no_one.exists())

    def test_follow_api_endpoint(self):
        client = self.get_client()
        response = client.post(
            f"/api/profiles/{self.user_v2.username}/follow/",
            {"action": "follow"}
        )
        r_data = response.json()
        count = r_data.get("followers")
        self.assertEqual(count, 1)
    
    def test_unfollow_api_endpoint(self):
        first = self.user
        second = self.user_v2
        first.profile.followers.add(second)

        client = self.get_client()
        response = client.post(
            f"/api/profiles/{self.user_v2.username}/follow/",
            {"action": "unfollow"}
        )
        r_data = response.json()
        count = r_data.get("followers")
        self.assertEqual(count, 0)

    def test_cannot_follow_api_endpoint(self):
        client = self.get_client()
        response = client.post(
            f"/api/profiles/{self.user.username}/follow/",
            {"action": "follow"}
        )
        r_data = response.json()
        count = r_data.get("followers")
        self.assertEqual(count, 0)