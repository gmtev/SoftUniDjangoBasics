from django import forms
from examDjangoBasics.posts.models import Post
from examDjangoBasics.mixins import ReadOnlyMixin


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author', 'updated_at')


class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):

        labels = {
            'title': 'Title:',
            'image_url': 'Post Image URL:',
            'content': 'Content:',
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Put an attractive and unique title...',
            }),

            'content': forms.Textarea(attrs={
                'placeholder': 'Share some interesting facts about your adorable pets...',
            }),
        }

        help_texts = {
            'image_url': 'Share your funniest furry photo URL!',
        }
        error_messages = {
                  'title': {
             'unique': "Oops! That title is already taken. How about something fresh and fun?",
            },
        }


class PostEditForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
            labels = {
                'title': 'Title:',
                'image_url': 'Post Image URL:',
                'content': 'Content:',
            }


class PostDeleteForm(ReadOnlyMixin, PostBaseForm):
    read_only_fields = ['title', 'image_url', 'content',]

    class Meta(PostBaseForm.Meta):
            labels = {
                'title': 'Title:',
                'image_url': 'Post Image URL:',
                'content': 'Content:',
            }