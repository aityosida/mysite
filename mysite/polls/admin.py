from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import Question,Choice,CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('age',)}),)
    list_display = ['username', 'email', 'age']

admin.site.register(CustomUser,CustomUserAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date']
    list_display_links = ('question_text', )

admin.site.register(Question)

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['choice_text', 'vote']
    list_display_links = ('choice_text', )
    raw_id_fields = ('question',)

admin.site.register(Choice)
