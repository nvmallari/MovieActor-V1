from django.urls import path

from . import views
from movieactor import views

app_name = 'movieactor'

urlpatterns = [
    path('', views.movieactor_home, name='home'),
    #path('get-name/', views.get_name, name='get-name'),
]

