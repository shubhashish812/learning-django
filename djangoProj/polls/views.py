from django.http import HttpResponse
from django.shortcuts import render
from .models import Question


def index(request):
    questions = Question.objects.order_by("-dt")[:5]
    print(questions)
    context = {
        "questions": questions,
    }
    return render(request, "polls/index.html", context)


def detail(request, q_id):
    return HttpResponse("Question: %s." % q_id)


def results(request, q_id):
    return HttpResponse("results on question: %s." % q_id)


def vote(request, q_id):
    return HttpResponse("voting on question: %s" % q_id)
