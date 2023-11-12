import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    ques = models.CharField(max_length=200)
    dt = models.DateTimeField("date published")

    def __str__(self):
        return self.ques

    def is_recent(self):
        return self.dt >= timezone.now()-datetime.timedelta(days=1)


class Choice(models.Model):
    q = models.ForeignKey(Question, on_delete=models.CASCADE)
    ans = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.ans
