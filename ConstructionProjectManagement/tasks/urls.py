from django.urls.conf import path, include

from tasks import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='tasks'),
    path('create/', views.TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/', include([
        path('detail/', views.TaskDetailView.as_view(), name='task-detail'),
        path('edit/', views.TaskEditView.as_view(), name='task-edit'),
        path('delete/', views.TaskDeleteView.as_view(), name='task-delete'),
    ])),
    # path('reports/', views.ReportListView.as_view(), name='reports'),
    path('report-add/', views.ReportCreateView.as_view(), name='report-add'),
    path('report/<int:rep_pk>/', include([
        path('detail/', views.ReportDetailView.as_view(), name='report-detail'),
        path('edit/', views.ReportEditView.as_view(), name='report-edit'),
        path('delete/', views.ReportDeleteView.as_view(), name='report-delete'),
    ]))

]