from django import forms
from musicAppExamPrep.albums.models import Album
from musicAppExamPrep.mixins import ReadOnlyMixin


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owner', )
        widgets = {
            'album_name': forms.TextInput(attrs={'placeholder': 'Album Name'}),
            'artist': forms.TextInput(attrs={'placeholder': 'Artist'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Image URL'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price'}),
        }


class AlbumCreateForm(AlbumBaseForm):
    pass


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumDeleteForm(ReadOnlyMixin, AlbumBaseForm):
    read_only_fields = ['album_name', 'artist', 'description', 'image_url', 'price']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the genre field to display as a CharField with readonly text
        self.fields['genre'] = forms.CharField(
            initial=self.instance.get_genre_display(),
            widget=forms.TextInput(attrs={'readonly': 'readonly'})
        )