from django.urls import reverse_lazy
from django.views.generic.edit import BaseFormView
from fruits.models import Fruit
from fruitipediaExamPrep.utils import get_user_obj
from django.views.generic import ListView, DetailView, DeleteView, TemplateView


# we'll write a function that returns Profile.objects.first() in a new utils.py file
# we use listview instead of template view, because the profile returns a list of all albums
# BaseFormView is used for the form
# we use album because the idea is that if there is no Profile you get a form to create one; if there is,
# you get the albums
# this logic can be stored in a separate app "commons"


class DashboardView(ListView):
    model = Fruit
    template_name = 'dashboard.html'
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data()
    #     context['profile'] = get_user_obj()
    #     return context                   no need since template tags

    # def get_template_names(self):
    #     profile = get_user_obj()  # none or queryset
    #
    #     if profile:
    #         return ['home-with-profile.html']
    #
    #     return ['home-no-profile.html']


class IndexView(TemplateView):
    template_name = 'index.html'
