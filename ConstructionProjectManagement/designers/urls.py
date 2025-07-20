
from django.urls.conf import path, include
from designers import views

urlpatterns = [
    path('', views.DesignerListView.as_view(), name='designers'),
    path('create/', views.DesignerCreateView.as_view(), name='designer-create'),
    path('<int:pk>/', include([
        path('details', views.DesignerDetailView.as_view(), name='designer-details'),
        path('edit/', views.DesignerEditView.as_view(), name='designer-edit'),
    ])),
]