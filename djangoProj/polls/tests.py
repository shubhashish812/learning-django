import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):
    def test_is_recent_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_ques = Question(dt=time)
        self.assertIs(future_ques.is_recent(), False)
