from django.contrib import admin
from .models import Question, Choice
from django.core.paginator import Paginator


class ChoicesInLine(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["ques", "dt", "is_recent"]
    list_filter = ["dt"]
    search_fields = ["ques"]
    search_help_text = "Enter your Question here"
    Paginator.list_per_page = 5
    fieldsets = [
        (None, {"fields": ["ques"]}),
        ("Date information", {"fields": ["dt"]}),
    ]
    inlines = [ChoicesInLine]


admin.site.register(Question, QuestionAdmin)
