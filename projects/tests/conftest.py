import pytest
from datetime import date
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from projects.models import Project

User = get_user_model()

# create a user object
@pytest.fixture
def user() -> User:
    return User.objects.create_user(username="testuser", password="testpassword")

# create a project object
@pytest.fixture
def project(user) -> Project:
    return Project.objects.create(
        name='Test Project',
        description='Test project description',
        start_date=date(2024, 3, 1),
        end_date=date(2024, 4, 1),
    )

@pytest.fixture()  
def api_client() -> APIClient:  
    """  
    Fixture to provide an API client  
    """  
    yield APIClient()

@pytest.fixture
def project_payload(user) -> dict:
    return {
        "name": "New project",
        "description": "Test project description",
        "start_date": "2024-01-01",
        "end_date": "2024-02-01",
        "team_members": [user.id]
    }