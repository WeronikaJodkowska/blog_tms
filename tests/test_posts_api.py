import pytest

from django.test.client import Client

from tests.factories import PostFactory, UserFactory


@pytest.mark.django_db
class TestPostsViews:
    def setup_method(self):
        self.client = Client()
        self.user = UserFactory()

    def test_posts_list(self):
        self.client.force_login(self.user)

        PostFactory.create_batch(15)
        response = self.client.get("/api/posts/")

        assert response.status_code == 200
        assert len(response.data["results"]) == 10
        assert response.data["count"] == 15

    def test_posts_create(self):
        self.client.force_login(self.user)

        data = {"title": "title", "slug": "slug", "text": "text"}
        response = self.client.post("/api/posts/", data=data)
        assert response.status_code == 201

        response = self.client.get("/api/posts/")
        assert response.status_code == 200
        assert len(response.data["results"]) == 1
        assert "image" in response.data["results"][0]