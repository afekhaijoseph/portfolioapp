from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import MyUser, Person, Occupation, Skills, WorkExp, AcadExp, Contact
from user.forms import UserRegisterForm, CustomUserChangeForm


class MyUserAdmin(UserAdmin):
    add_form = UserRegisterForm
    form = CustomUserChangeForm
    model = MyUser
    list_display = ['username', "email"]

admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Person)
admin.site.register(Occupation)
admin.site.register(Skills)
admin.site.register(WorkExp)
admin.site.register(AcadExp)
admin.site.register(Contact)

