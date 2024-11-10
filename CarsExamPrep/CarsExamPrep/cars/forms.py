from django import forms
from CarsExamPrep.mixins import ReadOnlyMixin
from CarsExamPrep.cars.models import Car


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        exclude = ['owner']


class CarCreateForm(CarBaseForm):
    class Meta(CarBaseForm.Meta):
        fields = ['type', 'model', 'year', 'image_url', 'price']
        labels = {
            'type': 'Type:',
            'model': 'Model:',
            'year': 'Year:',
            'image_url': 'Image URL:',
            'price': 'Price:'
        }
        widgets = {
            'image_url': forms.URLInput(attrs={'placeholder': 'https://...'})
        }
        error_messages = {
            'image_url': {
                'unique': "This image URL is already in use! Provide a new one.",
            },
            'price': {
                'min_value': "Price cannot be below 1.0.",
            }
        }


class CarEditForm(CarBaseForm):
    class Meta(CarBaseForm.Meta):
        fields = ['type', 'model', 'year', 'image_url', 'price']
        labels = {
            'type': 'Type:',
            'model': 'Model:',
            'year': 'Year:',
            'image_url': 'Image URL:',
            'price': 'Price:'
        }
        error_messages = {
            'image_url': {
                'unique': "This image URL is already in use! Provide a new one.",
            },
            'price': {
                'min_value': "Price cannot be below 1.0.",
            }
        }


class CarDeleteForm(ReadOnlyMixin, CarBaseForm):
    class Meta(CarBaseForm.Meta):
        fields = ['type', 'model', 'year', 'image_url', 'price']

    read_only_fields = ['type', 'model', 'year', 'image_url', 'price', ]