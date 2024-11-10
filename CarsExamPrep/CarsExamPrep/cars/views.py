from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from CarsExamPrep.cars.forms import CarCreateForm, CarEditForm, CarDeleteForm
from CarsExamPrep.cars.models import Car
from CarsExamPrep.utils import get_user_obj


class CarCatalogueView(ListView):
    model = Car
    template_name = 'catalogue.html'


class CarCreateView(CreateView):
    model = Car
    form_class = CarCreateForm
    template_name = 'car-create.html'
    success_url = reverse_lazy('car-catalogue')

    def form_valid(self, form):
        form.instance.owner = get_user_obj()
        return super().form_valid(form)


class CarDetailsView(DetailView):
    model = Car
    template_name = 'car-details.html'
    pk_url_kwarg = 'id'


class CarEditView(UpdateView):
    model = Car
    form_class = CarEditForm
    pk_url_kwarg = 'id'
    template_name = 'car-edit.html'
    success_url = reverse_lazy('car_catalogue')


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car-delete.html'
    success_url = reverse_lazy('car-catalogue')
    pk_url_kwarg = 'id'
    form_class = CarDeleteForm
    # in order to fill the info

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)