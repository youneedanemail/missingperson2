from django.urls import path
from .views import indexPageView, dataView, personView, donatePageView

urlpatterns = [
    path("", indexPageView, name="index"),   
    path("datatable", dataView, name="datatable"), 
    path("person", personView, name="personinfo"),
    path("donate", donatePageView, name="donate"),
]     
