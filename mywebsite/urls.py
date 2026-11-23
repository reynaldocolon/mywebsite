from django.contrib import admin
from django.urls import path
from pages.views import home, about, projects, resources, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('projects/', projects, name='projects'),
    path('resources/', resources, name='resources'),
    path('contact/', contact, name='contact'),
]
