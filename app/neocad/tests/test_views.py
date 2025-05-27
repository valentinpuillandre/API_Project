from rest_framework.test import APITestCase, APIClient
from django.test import TestCase
from django.urls import reverse


class PingTestCase(TestCase):
    def test_ping(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})


class TestViews(APITestCase):
    """
    Test the views of the neocad app.
    """
    def test_home_view(self):
        """
        Test the viewers view.
        """
        client = APIClient()
        res = client.get("/nonconformity/")

        self.assertEqual(res.status_code, 200)
