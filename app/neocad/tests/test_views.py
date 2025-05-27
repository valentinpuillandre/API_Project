from rest_framework.test import APITestCase, APIClient


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
