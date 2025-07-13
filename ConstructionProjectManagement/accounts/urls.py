from tempfile import template

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from accounts import views

urlpatterns = [
    path("register/", views.NewAccountView.as_view(), name='new-account'),
    path("login/", LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("profile/<int:pk>/", include([
        path('', views.DetailProfileView.as_view(), name='profile-details'),
        path('edit/', views.EditProfileView.as_view(), name='profile-edit'),
        path('delete/', views.delete_profile_view, name='profile-delete'),
    ])),
]