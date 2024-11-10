from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from fruitipediaExamPrep.utils import get_user_obj
from fruits.models import Fruit
from fruits.forms import FruitCreateForm, FruitDeleteForm, FruitEditForm


class FruitCreateView(CreateView):
    model = Fruit
    form_class = FruitCreateForm
    template_name = 'create-fruit.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class FruitEditView(UpdateView):
    model = Fruit
    form_class = FruitEditForm
    pk_url_kwarg = 'id'
    template_name = 'edit-fruit.html'
    success_url = reverse_lazy('dashboard')


class FruitDetailsView(DetailView):
    model = Fruit
    template_name = 'details-fruit.html'
    pk_url_kwarg = 'id'


class FruitDeleteView(DeleteView):
    model = Fruit
    template_name = 'delete-fruit.html'
    success_url = reverse_lazy('dashboard')
    pk_url_kwarg = 'id'
    form_class = FruitDeleteForm
    # in order to fill the info

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)