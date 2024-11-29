from django.shortcuts import render, redirect
from .forms import AlbumForm
from .models import Album
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.
@method_decorator(login_required, name="dispatch")
class AddAlbumView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = "add_album.html"
    success_url = reverse_lazy("add_album")

    def form_valid(self, form):
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class UpdateAlbumView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = "add_album.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("homepage")


@method_decorator(login_required, name="dispatch")
class DeleteAlbumView(DeleteView):
    model = Album
    template_name = "delete_album.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("homepage")


def delete_album(request, id):
    album = Album.objects.get(pk=id)
    album.delete()
    return redirect("homepage")
