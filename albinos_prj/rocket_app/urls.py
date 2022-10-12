from django.urls import path
from . import views

app_name = 'rocket_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('isnewyear', views.is_newyear, name='newyear')
]