from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from accounts.forms import AppUserCreationForm, AppUserChangeForm
from accounts.models import Profile

# Register your models here.


UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(UserAdmin):
    list_display = ('email', 'is_active', 'is_staff',)
    form = AppUserChangeForm
    add_form = AppUserCreationForm

    fieldsets = (
        (None, {"fields": ("email", "password", 'username')}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    ordering = ("email",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['profiles_name', 'position', 'company_job']
    ordering = ('company_job', 'position')
    search_fields = ('company_job', 'position', 'first_name', 'last_name')