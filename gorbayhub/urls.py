from django.urls import path, include
from . import views
app_name = 'gorbayhub'

urlpatterns = [
    path('', views.home, name='Home'),
    path('Add/', views.add, name='Add'),
    path('Save', views.save, name='Save'),
    path('Post/<slug:slug>', views.post, name='Post'),
]
