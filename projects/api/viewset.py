from rest_framework import viewsets

from .serializers import ProjectSerializer
from projects.models import Project


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
