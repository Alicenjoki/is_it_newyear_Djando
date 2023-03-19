from . import views
from django.urls import path

urlpatterns =[
    path("", views.new_year, name="new_year")
]