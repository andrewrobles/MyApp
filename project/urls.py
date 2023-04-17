from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('todo/', include('MyApp.urls')),
    path('admin/', admin.site.urls),
]
