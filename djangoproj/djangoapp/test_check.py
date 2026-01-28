import pytest
from django.test import Client
import json

@pytest.mark.django_db
def test_db():
   client = Client()
   response = client.get("/api/health/")
   assert response.status_code==200
   assert response.json() == {"status": "DB is up"}
