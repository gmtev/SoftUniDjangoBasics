from django.urls import reverse_lazy
from django.views.generic.edit import BaseFormView
from musicAppExamPrep.profiles.forms import ProfileCreateForm
from musicAppExamPrep.albums.models import Album
from musicAppExamPrep.utils import get_user_obj
from django.views.generic import ListView, DetailView, DeleteView


# we'll write a function that returns Profile.objects.first() in a new utils.py file
# we use listview instead of template view, because the profile returns a list of all albums
# BaseFormView is used for the form
# we use album because the idea is that if there is no Profile you get a form to create one; if there is,
# you get the albums
# this logic can be stored in a separate app "commons"


class HomePage(ListView, BaseFormView):
    model = Album
    form_class = ProfileCreateForm
    success_url = reverse_lazy('home')

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data()
    #     context['profile'] = get_user_obj()
    #     return context                   no need since template tags

    def get_template_names(self):
        profile = get_user_obj()  # none or queryset

        if profile:
            return ['home-with-profile.html']

        return ['home-no-profile.html']

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProfileDetailView(DetailView):
    template_name = 'profile-details.html'
    # we do it like this since there is no profile authentication

    def get_object(self, queryset=None):
        return get_user_obj()


class ProfileDeleteView(DeleteView):
    template_name = 'profile-delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_user_obj()

