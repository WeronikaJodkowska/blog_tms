import faker
from django.test.client import Client

from tests.factories import UserFactory

import pytest


@pytest.mark.django_db
class TestAuthViews:
    def setup_method(self):
        self.client = Client()
        self.fake = faker.Faker()

        self.user = UserFactory()
        self.user.set_password("password")
        self.user.save()

    def test_register(self):
        data = {
            "email": self.fake.email(),
            "password": self.fake.md5(),
            "first_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
        }
        response = self.client.post("/api/register/", data=data)
        assert response.status_code == 201

        response = self.client.post("/api/login/", data=data)
        assert response.status_code == 200
        assert "token" in response.data

    def test_login(self):
        data = {
            "email": self.user.email,
            "password": "password",
        }
        response = self.client.post("/api/login/", data=data)
        assert response.status_code == 200
        assert "token" in response.data
