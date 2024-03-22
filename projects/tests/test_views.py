# test_views.py
import pytest
import logging

logger = logging.getLogger(__name__)

# @pytest.mark.django_db
# def test_create_project(api_client, project_payload) -> None:
#     # create a new project
#     response_create = api_client.post('/api/project/', data=project_payload, format="json")
#     logger.info(f"{response_create.data}")
#     assert response_create.status_code == 201 
#     assert response_create.data['data']['name'] == project_payload['name']

#     # read the newly created project
#     response_read = api_client.get('/api/project/', format="json")
#     assert response_read.status_code == 200
#     assert response_read.data['data'][0]['name'] == project_payload['name']



# @pytest.mark.django_db
# def test_update_project(api_client, project_payload) -> None:
#     # create a project
#     response_create = api_client.post('/api/project/', data=project_payload, format="json")
#     project_id = response_create.data["data"]["id"]
#     logger.info(f"Successfullly created project with ID {project_id}")
#     assert response_create.status_code == 201 
#     assert response_create.data['data']['name'] == project_payload['name']

#     # update the project
#     project_payload["name"]="Updated project name"
#     response_update = api_client.patch(f'/api/project/modify/{project_id}/', data=project_payload, format="json")
#     new_title = response_update.data['data']['name']
#     logger.info(f"Successfullly updated project with ID {project_id}")
#     logger.info(f"new project title is {new_title}")
#     assert response_update.status_code == 201 
#     assert response_update.data['data']['name'] == project_payload['name']

#     # project not found
#     response_update = api_client.patch(f'/api/project/modify/{project_id+20}/', data=project_payload, format="json")
#     assert response_update.status_code == 404
#     logger.info(f"Cound not find project with id {project_id+20}")

# @pytest.mark.django_db
# def test_delete_project(api_client, project_payload):
#     # create a project
#     response_create = api_client.post('/api/project/', data=project_payload, format="json")
#     project_id = response_create.data["data"]["id"]
#     logger.info(f"Successfullly created project with ID {project_id}")
#     assert response_create.status_code == 201 

#     # delete project
#     response_delete = api_client.delete(f"/api/project/modify/{project_id}/", data=project_payload, format="json")
#     logger.info(f"Deleted task with ID {project_id}")
#     assert response_delete.status_code == 204

#     # Read the project to ensure it was deleted
#     response_read = api_client.get(f"/api/project/modify/{project_id}/", format="json")
#     assert response_read.status_code == 404

#     # project not found
#     response_delete = api_client.delete(f'/api/project/modify/{project_id+20}/', data=project_payload, format="json")
#     assert response_delete.status_code == 404
#     logger.info(f"Cound not find project with id {project_id+20}")



@pytest.mark.django_db
def test_create_project_authenticated(api_client, project_payload, user):
    # authenticate the user
    api_client.force_authenticate(user=user)
    
    # send a post request with the authenticated user
    response_create = api_client.post('/api/project/', data=project_payload, format="json")
    assert response_create.status_code == 201

@pytest.mark.django_db
def test_create_project_unauthenticated(api_client, project_payload):
    
    # send a post request with the unauthenticated user
    response_create = api_client.post('/api/project/', data=project_payload, format="json")
    assert response_create.status_code == 403
