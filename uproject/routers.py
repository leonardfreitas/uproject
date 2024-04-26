from rest_framework.routers import SimpleRouter

from projects.api.viewset import ProjectViewSet

routers = SimpleRouter()

routers.register('projects', ProjectViewSet, basename='project')

urls = routers.urls