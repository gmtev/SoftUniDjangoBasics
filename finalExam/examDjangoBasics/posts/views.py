from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from examDjangoBasics.posts.forms import PostCreateForm, PostEditForm, PostDeleteForm
from examDjangoBasics.posts.models import Post
from examDjangoBasics.utils import get_user_obj


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'create-post.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.author = get_user_obj()
        return super().form_valid(form)


class PostEditView(UpdateView):
    model = Post
    form_class = PostEditForm
    pk_url_kwarg = 'id'
    template_name = 'edit-post.html'
    success_url = reverse_lazy('dashboard')


class PostDetailsView(DetailView):
    model = Post
    template_name = 'details-post.html'
    pk_url_kwarg = 'id'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete-post.html'
    success_url = reverse_lazy('dashboard')
    pk_url_kwarg = 'id'
    form_class = PostDeleteForm

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

