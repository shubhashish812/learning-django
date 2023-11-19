import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone


class Question(models.Model):
    ques = models.CharField(max_length=200, verbose_name="Question")
    dt = models.DateTimeField("date published")

    def __str__(self):
        return self.ques

    @admin.display(boolean=True, ordering=dt, description="Recent?")
    def is_recent(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.dt <= now


class Choice(models.Model):
    q = models.ForeignKey(Question, on_delete=models.CASCADE)
    ans = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.ans
