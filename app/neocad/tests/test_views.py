from rest_framework.test import APITestCase, APIClient
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken
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
    def setUp(self):
        self.client = APIClient()
        user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        token = AccessToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(token))

    def test_home_view(self):
        res = self.client.get("/api/nonconformity/")
        self.assertEqual(res.status_code, 200)


class NonConformityCRUDTestCase(APITestCase):
    def setUp(self):
        NonConformity.objects.all().delete()
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
        user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        token = AccessToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(token))

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


class NonConformityStatsTestCase(APITestCase):
    def setUp(self):
        NonConformity.objects.all().delete()
        # Create test user and get token
        user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        token = AccessToken.for_user(user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(token))

        # Create test data with different severity levels
        self.test_data = [
            {
                "company_id": "123",
                "site_id": "456",
                "reported_by": "test1@example.com",
                "issue_type": "Type A",
                "description": "Test description 1",
                "severity": "High",
                "status": "Open"
            },
            {
                "company_id": "123",
                "site_id": "456",
                "reported_by": "test2@example.com",
                "issue_type": "Type B",
                "description": "Test description 2",
                "severity": "High",
                "status": "Open"
            },
            {
                "company_id": "123",
                "site_id": "456",
                "reported_by": "test3@example.com",
                "issue_type": "Type C",
                "description": "Test description 3",
                "severity": "Medium",
                "status": "Open"
            },
            {
                "company_id": "123",
                "site_id": "456",
                "reported_by": "test4@example.com",
                "issue_type": "Type D",
                "description": "Test description 4",
                "severity": "Low",
                "status": "Open"
            }
        ]

        # Create non-conformities
        for data in self.test_data:
            NonConformity.objects.create(**data)

        self.stats_url = reverse('nonconformity-stats-severity')

    def test_severity_stats(self):
        """Test that the severity statistics endpoint returns correct counts"""
        response = self.client.get(self.stats_url)

        # Check response status
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that we got the expected counts
        self.assertEqual(response.data['High'], 2)
        self.assertEqual(response.data['Medium'], 1)
        self.assertEqual(response.data['Low'], 1)

        # Check that results are sorted by count (descending)
        counts = list(response.data.values())
        self.assertEqual(counts, sorted(counts, reverse=True))

    def test_severity_stats_unauthorized(self):
        """Test that unauthorized users cannot access the stats"""
        # Remove authentication
        self.client.credentials()

        response = self.client.get(self.stats_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
