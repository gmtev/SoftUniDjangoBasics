from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from musicAppExamPrep.utils import get_user_obj
from musicAppExamPrep.albums.forms import AlbumCreateForm, AlbumEditForm, AlbumDeleteForm
from musicAppExamPrep.albums.models import Album


class AlbumCreateView(CreateView):
    model = Album
    form_class = AlbumCreateForm
    template_name = 'album-add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class AlbumEditView(UpdateView):
    model = Album
    form_class = AlbumEditForm
    pk_url_kwarg = 'id'
    template_name = 'album-edit.html'
    success_url = reverse_lazy('home')


class AlbumDetailsView(DetailView):
    model = Album
    template_name = 'album-details.html'
    pk_url_kwarg = 'id'


class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'album-delete.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    form_class = AlbumDeleteForm
    # in order to fill the info

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

    # since is_valid tries to validate each field and checks for an existing name, which creates data duplication

