from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from accounts.forms import AppUserCreationForm, ProfileEditForm, ProfileDeleteForm
from accounts.models import Profile

# Create your views here.
UserModel = get_user_model()


class NewAccountView(CreateView):
    model = UserModel
    form_class = AppUserCreationForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)

        if response.status_code in [301, 302]:
            login(self.request, self.object)

        return response
    # function in signals.py receiver signal to create a new profile form without data when a new user is created !!!


class DetailProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile-detail.html'
    pk_url_kwarg = 'pk'


class EditProfileView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/profile-edit.html'
    pk_url_kwarg = 'pk'

    def test_func(self):
        profile_object = self.get_object()
        return self.request.user == profile_object.user
        # return self.request.user.pk == self.kwargs['pk']

    def get_context_data(self, **kwargs):
        profile = self.get_object()
        kwargs.update({'profile': profile})
        return super().get_context_data(**kwargs)

    def get_success_url(self) -> str:
        return reverse(
            'profile-details',
            kwargs={
                'pk': self.object.pk,
            }
        )


class DeleteProfileView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    template_name = 'accounts/profile-delete.html'
    success_url = reverse_lazy('home')
    form_class = ProfileDeleteForm
    pk_url_kwarg = 'pk'

    def test_func(self):
        profile_object = self.get_object()
        return self.request.user == profile_object.user
        # return self.request.user.pk == self.kwargs['pk']

    def get_initial(self) -> dict:
        return self.object.__dict__

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"data": self.get_initial()})
        return kwargs
