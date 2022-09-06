import pytest

from django.test.client import Client


@pytest.mark.django_db
class TestViews:
    def setup_method(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get("/")
        assert response.status_code == 200
