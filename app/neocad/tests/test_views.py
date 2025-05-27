from rest_framework.test import APITestCase, APIClient
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from ..models import NonConformity


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


class NonConformityCRUDTestCase(APITestCase):
    def setUp(self):
        self.non_conformity = NonConformity.objects.create(
            company_id="123",
            site_id="456",
            reported_by="test@example.com",
            issue_type="Type A",
            description="Test description",
            severity="High",
            status="Open"
        )
        self.list_url = reverse('nonconformity-list')
        self.detail_url = reverse(
            'nonconformity-detail', args=[self.non_conformity.id]
            )

    def test_create_non_conformity(self):
        data = {
            "company_id": "789",
            "site_id": "101",
            "reported_by": "new@example.com",
            "issue_type": "Type B",
            "description": "New description",
            "severity": "Low",
            "status": "Closed"
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_non_conformity(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data['company_id'], self.non_conformity.company_id
            )

    def test_patch_non_conformity(self):
        data = {
            "reported_by": "updated@example.com"
        }
        response = self.client.patch(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['reported_by'], "updated@example.com")

    def test_delete_non_conformity(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(
            NonConformity.objects.filter(id=self.non_conformity.id).exists()
            )
