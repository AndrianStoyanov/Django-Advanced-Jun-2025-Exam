from django.urls.conf import path, include

from projects import views

urlpatterns = [
    path('create/', views.CreateProjectView.as_view(), name='project-create'),
    path('int:pro_pk', include([
        path('details/', views.DetailsProjectView.as_view(), name='project-details'),
        path('edit/', views.EditProjectView.as_view(), name='project-edit'),
        path('delete/', views.DeleteProjectView.as_view(), name='project-delete'),
    ]))

]