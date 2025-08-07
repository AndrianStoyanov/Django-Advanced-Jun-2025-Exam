from django.urls.conf import path

from common import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('home-ex/', views.HomeExView.as_view(), name='home-ex'),
]