from django.urls import path

from .views import ProjectListCreateView, ProjectRetrieveUpdateDeleteView

urlpatterns = [
    path('project/', ProjectListCreateView.as_view(), name="list-create"),
    path('project/modify/<int:project_id>/', ProjectRetrieveUpdateDeleteView.as_view(), name="project-retrieve-update-delete")
]