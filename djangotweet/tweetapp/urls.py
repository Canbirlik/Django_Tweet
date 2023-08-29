from django.urls import path
from . import views

app_name = "tweetapp"

urlpatterns = [
    path("", views.listtweet, name="listtweet"),
    path("addtweet/", views.addtweet, name="addtweet"),
    path("listtweet/", views.listtweet, name="listtweet section"),
    path("addtweetbyform/", views.addtweet_byform, name="addtweetbyform"),
    path("addtweetbymodelform/", views.addtweet_bymodelform, name="addtweetbymodelform"),
]