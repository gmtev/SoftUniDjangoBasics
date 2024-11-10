from django import forms

from CarsExamPrep.profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'



class ProfileCreateForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        fields = ['username', 'email', 'age', 'password']
        help_texts = {
            'age': "Age requirement: 21 years and above.",
        }
        labels = {
            'username': 'Username:',
            'age': 'Age:',
            'password': 'Password:',
            'email': 'Email:',
        }
        widgets = {
            'password': forms.PasswordInput(),
        }



class ProfileEditForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        labels = {
            'username': 'Username:',
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'profile_picture': 'Profile Picture:',
            'age': 'Age:',
            'password': 'Password:',
            'email': 'Email:',
        }


    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['password'].initial = self.instance.password


