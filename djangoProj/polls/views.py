from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Question, Choice


def index(request):
    questions = Question.objects.order_by("-dt")[:5]
    print(questions)
    context = {
        "questions": questions,
    }
    return render(request, "polls/index.html", context)


def detail(request, q_id):
    try:
        question = Question.objects.get(pk=q_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return render(request, "polls/detail.html", {"question": question})


def results(request, q_id):
    question = get_object_or_404(Question, pk=q_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, q_id):
    question = get_object_or_404(Question, pk=q_id)
    try:
        sel_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):

        return render(request, "polls/detail.html",
                      {
                          "question": question,
                          "error_message": "Didnt select choice"
                      },
                      )
    else:
        sel_choice.votes += 1
        sel_choice.save()
        # Sending redirect to ensure data doesn't post twice if back button is pressed
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

