import pytest

from django.test import TestCase, Client
from .models import Category


client = Client()


@pytest.mark.django_db
def test_category_model():
    category = Category.objects.create(name="TV show", slug="tv-show")
    assert category.name == "TV show"


def test_request():
    resp = client.get('/')
    assert resp.status_code == 200
