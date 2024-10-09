from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group, User
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm, ActionForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from unfold.admin import ModelAdmin



# admin.site.register(Country)
# admin.site.register(InnovationPractice)
# admin.site.register(Message)


admin.site.unregister(Group)


admin.site.unregister(User)

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    action_form = ActionForm
    fieldsets = (
        ("Important datas", {'fields': ('username', 'password', "is_superuser", "is_active", "is_staff")}),
        ('Important dates', {'fields': ('last_login',"date_joined")}),
    )
    list_display = ["username"]
    readonly_fields = ["last_login", "date_joined"]


@admin.register(Country)
class CountryAdmin(ModelAdmin):
    search_fields = ["name_tk", "name_en", "name_ja"]


@admin.register(InnovationPractice)
class InnovationPracticeAdmin(ModelAdmin):
    search_fields = ["country__name_tk", "country__name_en", "country__name_ja"]


@admin.register(Message)
class MessageAdmin(ModelAdmin):
    search_fields = ["title", "fullname"]