from django import forms
from fruits.models import Fruit
from fruitipediaExamPrep.mixins import ReadOnlyMixin


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ('owner',)


class FruitCreateForm(FruitBaseForm):
    class Meta:
        model = Fruit
        exclude = ('owner',)
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Fruit Name',
                'class': 'form-control',
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'Fruit Image URL',
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Fruit Description',
                'class': 'form-control',
                'rows': 4,
            }),
            'nutrition': forms.Textarea(attrs={
                'placeholder': 'Nutrition Info',
                'class': 'form-control',
                'rows': 2,
            }),
        }


class FruitEditForm(FruitBaseForm):
    class Meta:
        model = Fruit
        exclude = ('owner',)
        labels = {
            'name': 'Name:',
            'image_url': 'Image URL:',
            'description': 'Description:',
            'nutrition': 'Nutrition:',
        }


class FruitDeleteForm(ReadOnlyMixin, FruitBaseForm):
    model = Fruit
    exclude = ('owner',)
    read_only_fields = ['name', 'nutrition', 'description', 'image_url',]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # Set the genre field to display as a CharField with readonly text
    #     self.fields['genre'] = forms.CharField(
    #         initial=self.instance.get_genre_display(),
    #         widget=forms.TextInput(attrs={'readonly': 'readonly'})
    #     )