
from django.urls.conf import path, include
from builders import views

urlpatterns = [
    path('', views.BuilderListView.as_view(), name='builders'),
    path('create/', views.BuilderCreateView.as_view(), name='builder-create'),
    path('<int:pk>/', include([
        path('details', views.BuilderDetailView.as_view(), name='builder-details'),
        path('edit/', views.BuilderEditView.as_view(), name='builder-edit'),
    ])),
]