from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from accounts.models import Profile
from core.mixins import ReadOnlyFieldsMixin

UserModel = get_user_model()


class AppUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email', 'username')

        help_texts = {
            'username': 'Username must be unique',
            'password': 'Password must be with letters, number and special characters',
            'email': 'Email must be unique',
        }


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'profile_picture': 'Profile Picture:',
            'position': 'Position:',
            'company_job': 'Company:',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter a first name...'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter a last name...'}),
            'profile_picture': forms.URLInput(attrs={'placeholder': 'Upload a photo...'}),
            'position': forms.TextInput(attrs={'placeholder': 'Enter a position...'}),
            'company_job': forms.TextInput(attrs={'placeholder': 'Enter a company...'}),
        }


class ProfileEditForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ReadOnlyFieldsMixin, ProfileBaseForm):
    pass