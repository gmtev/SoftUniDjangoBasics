from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from fruitipediaExamPrep.utils import get_user_obj
from profiles.forms import ProfileCreateForm, ProfileEditForm
from profiles.models import Profile


# Create your views here.
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'create-profile.html'
    success_url = reverse_lazy('dashboard')


    # if baseformview is used
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'edit-profile.html'
    success_url = reverse_lazy('details-profile')

    def get_object(self, queryset=None):
        return get_user_obj()

class ProfileDetailsView(DetailView):
    model = Profile

    template_name = 'details-profile.html'

    def get_object(self, queryset=None):
        return get_user_obj()


class ProfileDeleteView(DeleteView):

    template_name = 'delete-profile.html'

    def get_success_url(self):
        return reverse('index')

    def get_object(self, queryset=None):
        return get_user_obj()
