from django.urls import path
from . import views

urlpatterns = [
    path("", views.visitor, name="homepage"),
    path("delete-session/", views.delete_session_item, name="delete_session")
]
