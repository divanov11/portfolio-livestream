from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name="home"),
    path('project/<str:pk>/', views.projectPage, name="project"),

    path('add-project/', views.addProject, name="add-project"),
    path('edit-project/<str:pk>/', views.editProject, name="edit-project"),
]
