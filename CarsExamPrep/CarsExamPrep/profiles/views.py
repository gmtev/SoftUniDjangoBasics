from django.db.models import Sum
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from CarsExamPrep.profiles.forms import ProfileCreateForm, ProfileEditForm
from CarsExamPrep.profiles.models import Profile
from CarsExamPrep.cars.models import Car
from CarsExamPrep.utils import get_user_obj


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'profile-create.html'
    success_url = reverse_lazy('car_catalogue')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile-details.html'

    def get_object(self, queryset=None):
        return get_user_obj()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        total_sum = Car.objects.filter(owner=profile).aggregate(total_price=Sum('price'))['total_price'] or 0
        context['total_sum'] = total_sum
        return context


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profile-edit.html'
    success_url = reverse_lazy('profile-details')

    def get_initial(self):
        return self.object.__dict__

    def get_object(self, queryset=None):
        return get_user_obj()


class ProfileDeleteView(DeleteView):

    template_name = 'profile-delete.html'

    def get_success_url(self):
        return reverse('index')

    def get_object(self, queryset=None):
        return get_user_obj()