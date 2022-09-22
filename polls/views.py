"""Views of polls app."""
from django.utils import timezone
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Choice, Question, Vote

def get_queryset(self):
    """Get queryset function.

    :return the last five published questions.
    (not including those set to be published in the future).
    """
    return Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]


class IndexView(generic.ListView):
    """Question index page that display the latest question."""

    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """:return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()
                                       ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    """Detail view class."""
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """Excludes any questions that aren't published yet."""
        return Question.objects.filter(pub_date__lte=timezone.now())

    def get(self, request, question_id):
        """Question detail page that can vote the question."""
        try:
            question = get_object_or_404(Question, pk=question_id)
        except Http404:
            messages.error(request, f"Poll does not exists.")
            return redirect('polls:index')
        if not question.can_vote():
            messages.error(request, 'Voting is not allowed!')
            return redirect('polls:index')
        try:
            prev_choice = question.vote_set.get(user=request.user, question=question).choice
        except (KeyError, Vote.DoesNotExist):
            return render(request, 'polls/detail.html', {'question': question})
        return render(request, 'polls/detail.html', {'question': question, 'previous_choice': prev_choice})


class ResultsView(generic.DetailView):
    """Question results page that display the score vote of the question."""

    model = Question
    template_name = 'polls/results.html'

@login_required(login_url='/accounts/login/')
def vote(request, question_id):
    """Vote function that increase a value of vote and save to vote result."""
    user = request.user
    print("current user is", user.id, 'login', user.username)
    print("Real name:", user.first_name, user.last_name)
    if not user.is_authenticated:
        return redirect('login')
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    try:
        vote_object = Vote.objects.get(user=user, question=question)
        vote_object.choice = selected_choice
        vote_object.save()
    except Vote.DoesNotExist:
        Vote.objects.create(user=user, choice=selected_choice, question=question).save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
