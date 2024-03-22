from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Project
from .serializers import ProjectSerializer


class ProjectListCreateView(GenericAPIView):
    serializer_class = ProjectSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly] # uncomment to incluse permission restrictions

    def get(self, request:Request):
        projects = Project.objects.all()
        serializer = self.serializer_class(instance=projects, many=True)
        response = {
            "message":"successful",
            "data":serializer.data
        }
        return Response(data=response, status=status.HTTP_200_OK)
    
    def post(self, request:Request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "message":"successful",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        
        response = {
            "message":"failed",
            "data":serializer.errors
        }
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)


class ProjectRetrieveUpdateDeleteView(GenericAPIView):
    serializer_class = ProjectSerializer

    def get(self, request:Request, project_id:int):
        project = get_object_or_404(Project, id=project_id)

        serializer = self.serializer_class(instance=project)
        response = {
                "message":"successful",
                "data":serializer.data
            }
        return Response(data=response, status=status.HTTP_200_OK)
    
    def patch(self, request:Request, project_id:int):
        project = get_object_or_404(Project, id=project_id)

        serializer = self.serializer_class(instance=project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message":"successful",
                "data":serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        response = {
            "message":"failed",
            "info":serializer.errors
        }
        return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request:Request, project_id:int):
        project = get_object_or_404(Project, id=project_id)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
