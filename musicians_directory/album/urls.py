from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.AddAlbumView.as_view(), name="add_album"),
    path("edit/<int:id>/", views.UpdateAlbumView.as_view(), name="edit_album"),
    path("delete/<int:id>/", views.DeleteAlbumView.as_view(), name="delete_album"),
]
