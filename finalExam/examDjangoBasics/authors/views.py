from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from examDjangoBasics.authors.forms import AuthorCreateForm, AuthorEditForm
from examDjangoBasics.authors.models import Author
from examDjangoBasics.posts.models import Post
from examDjangoBasics.utils import get_user_obj



class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorCreateForm
    template_name = 'create-author.html'
    success_url = reverse_lazy('dashboard')


class AuthorEditView(UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = 'edit-author.html'
    success_url = reverse_lazy('details-author')

    def get_object(self, queryset=None):
        return get_user_obj()


class AuthorDetailsView(DetailView):
    model = Author

    template_name = 'details-author.html'

    def get_object(self, queryset=None):
        return get_user_obj()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_post = Post.objects.order_by('-updated_at').first()
        context['latest_post'] = latest_post
        return context

class AuthorDeleteView(DeleteView):

    template_name = 'delete-author.html'

    def get_success_url(self):
        return reverse('index')

    def get_object(self, queryset=None):
        return get_user_obj()