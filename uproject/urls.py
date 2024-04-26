from django.contrib import admin
from django.urls import path, include

from teams.views import hello
from .routers import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello, name='hello'),
    path('core/', include('core.urls', namespace='core')),
    path('api/', include(urls)),
]
