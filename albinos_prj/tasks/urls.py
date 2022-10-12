from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    path("tasks/", views.index, name='index'),
    path("add/", views.form_page, name='add'),
    path("", views.main, name='main')
]