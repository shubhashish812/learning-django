import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):
    def test_is_recent_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_ques = Question(dt=time)
        self.assertIs(future_ques.is_recent(), False)

    def test_is_recent_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(dt=time)
        self.assertIs(old_question.is_recent(), False)

    def test_is_recent_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(dt=time)
        self.assertIs(recent_question.is_recent(), True)
