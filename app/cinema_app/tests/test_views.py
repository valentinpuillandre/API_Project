from rest_framework.test import APITestCase, APIClient


class TestViews(APITestCase):
    """
    Test the views of the cinema app.
    """
    def test_home_view(self):
        """
        Test the viewers view.
        """
        client = APIClient()
        res = client.get("/viewers/")

        self.assertEqual(res.status_code, 200)
