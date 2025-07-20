from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from designers.models import Designer
# Create your views here.


class DesignerListView(ListView):
    model = Designer
    template_name = 'designer/designers.html'


class DesignerCreateView(CreateView):
    model = Designer
    template_name = 'designer/designer-add.html'


class DesignerDetailView(DetailView):
    model = Designer
    template_name = 'designer/designer-details.html'


class DesignerEditView(UpdateView):
    model = Designer
    template_name = 'designer/designer-edit.html'