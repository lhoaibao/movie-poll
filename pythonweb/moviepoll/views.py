from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.urls import reverse
# Create your views here.
def index(request):
    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'lastest_question_list': lastest_question_list}
    return render(request, 'moviepoll/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'moviepoll/detail.html', {'question':question})


def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    total_vote = 0
    print(question.choice_set.all)
    for choice in question.choice_set.all():
        total_vote += choice.votes
    return render(request, 'moviepoll/result.html', {'question':question, 'total_vote':total_vote})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'moviepoll/detail.html', {'question':question,
                                                         'error_message': "You didn't select a choice"
                                                        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('moviepoll:result', args=(question.id,)))