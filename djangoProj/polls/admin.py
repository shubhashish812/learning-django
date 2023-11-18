from django.contrib import admin
from .models import Question, Choice


class ChoicesInLine(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["ques", "dt", "is_recent"]
    fieldsets = [
        (None, {"fields": ["ques"]}),
        ("Date information", {"fields": ["dt"]}),
    ]
    inlines = [ChoicesInLine]


admin.site.register(Question, QuestionAdmin)
