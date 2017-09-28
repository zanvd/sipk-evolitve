# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Answer, Question, Voter
from pprint import pprint


class IndexView(generic.ListView):
    template_name = 'evolitve_app/base.html'
    context_object_name = 'question_list'

    def get_queryset(self):
        closed_questions = list(Question.objects.filter(
            close_date__lte=timezone.now()
        ).order_by('close_date'))
        open_questions = Question.objects.filter(
            start_date__lte=timezone.now(),
            close_date__gt=timezone.now()
        ).order_by('close_date')

        # Mark the highest rated answer in closed questions.
        for index, question in enumerate(closed_questions):
            highest = question.answer_set.first()
            for answer in question.answer_set.all():
                if answer.votes > highest.votes:
                    highest = answer
            test = closed_questions[index].answer_set.get(pk=highest.id).set_highest()
            pprint(test.highest)

        return {'closed': closed_questions, 'open': open_questions}


class QuestionView(generic.DetailView):
    model = Question
    template_name = 'evolitve_app/question.html'

    def get_queryset(self):
        return Question.objects.filter(start_date__lte=timezone.now(), close_date__gte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'evolitve_app/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        answer = question.answer_set.get(pk=request.POST['answer'])
        voter = question.voter_set.get(uuid=request.POST['uuid'], emso=request.POST['emso'])
    except (KeyError, Answer.DoesNotExist):
        # Redisplay the voting form.
        return render(request, 'evolitve_app/question.html', {
            'question': question,
            'uuid': request.POST.get('uuid', ''),
            'error_message': "Prosimo, izberite odgovor.",
        })
    except (KeyError, Voter.DoesNotExist):
        return render(request, 'evolitve_app/question.html', {
            'question': question,
            'error_message': 'Napačna identifikacija številka volivca.',
        })
    else:
        answer.votes += 1
        answer.save()
        # Use redirect to prevent voting twice with back button.
        return HttpResponseRedirect(reverse('evolitve_app:results', args=[question.id]))
