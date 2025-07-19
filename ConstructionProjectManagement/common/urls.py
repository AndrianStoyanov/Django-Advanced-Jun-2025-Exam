from django.urls.conf import path

from common import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
    path('home-ex/', views.HomeExView.as_view(), name='home-ex'),
    path('projects/', views.ProjectPageView.as_view(), name='projects'),
]