import pytest

from django.core.exceptions import ValidationError
from projects.models import Project

@pytest.mark.django_db
def test_project_duration(project) -> None:
    assert project.get_project_duration() == 31

@pytest.mark.django_db
def test_team_members_count(project, user) -> None:
    project.team_members.add(user)
    assert project.get_team_members_count() == 1

@pytest.mark.django_db
def test_project_name_character_count(project) -> None:
    project.name = 'A' * 256  # exceeds the max_length constraint

    with pytest.raises(ValidationError) as e:
        project.full_clean()

    assert 'Ensure this value has at most 100 characters' in str(e.value)