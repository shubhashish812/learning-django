from django.contrib import admin
from .models import Question

from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["ques"]}),
        ("Date information", {"fields": ["dt"]}),
    ]


admin.site.register(Question, QuestionAdmin)


