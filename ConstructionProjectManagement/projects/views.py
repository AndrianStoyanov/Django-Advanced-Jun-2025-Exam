
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView


# Create your views here.
class CreateProjectView(CreateView):
    ...


class DetailsProjectView(DetailView):
    ...


class EditProjectView(UpdateView):
    ...


class DeleteProjectView(DeleteView):
    ...