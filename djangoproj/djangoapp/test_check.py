import pytest
from django.test import Client
import json

@pytest.mark.django_db
def test_db():
   client = Client()
   response = client.get("/api/health/")
   assert response.status_code==200
   assert response.json() == {"status": "DB is up"}

@pytest.mark.django_db
def test_live():
    client = Client()
    response = client.get("/api/health/live")
    assert response.status_code==200
    assert response.json() == {"status":"running"}

@pytest.mark.django_db
def test_migrate():
    client = Client()
    response = client.get("/api/health/migration")
    assert response.status_code==200
