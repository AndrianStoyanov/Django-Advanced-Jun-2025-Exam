
from django.urls.conf import path, include

from supervisions import views

urlpatterns = [
    path('', views.SupervisionListView.as_view(), name='supervisions'),
    path('create/', views.SupervisionCreateView.as_view(), name='supervision-create'),
    path('<int:pk>/', include([
        path('details', views.SupervisionDetailView.as_view(), name='supervision-details'),
        path('edit/', views.SupervisionEditView.as_view(), name='supervision-edit'),
    ])),
]
