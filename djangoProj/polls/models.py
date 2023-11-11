from django.db import models


class Question(models.Model):
    q = models.CharField(max_length=200)
    dt = models.DateTimeField("date published")


class Choice(models.Model):
    q = models.ForeignKey(Question, on_delete=models.CASCADE)
    ans = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


