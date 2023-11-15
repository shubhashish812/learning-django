from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-dt")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


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
