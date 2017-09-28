# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Question(models.Model):
    """
    Question model:
    - id
    - question_text: question for the elections.
    - start_date: date of publishing (when the questionnaire is going to be visible).
    - close_date: date of closing (when the questionnaire is going to be closed).
    - voters_num: number of voters that are going to be answering on this question.
    """
    question_text = models.CharField(max_length=100)
    start_date = models.DateTimeField('published date')
    close_date = models.DateTimeField('closed date')
    voters_num = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.question_text

    # Retrieve total number of answers.
    def get_total_answered(self):
        total_votes = 0
        for answer in self.answer_set.all():
            total_votes += answer.votes
        return total_votes
    get_total_answered.short_description = 'Število odgovorov'


@python_2_unicode_compatible
class Answer(models.Model):
    """
    Answer model:
    - id
    - answer_text: text of the answer.
    - votes: number of votes for this answer.
    - question: foreign key of the question to which this answer belongs to.
    """
    answer_text = models.CharField(max_length=60)
    votes = models.PositiveIntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_text

    def set_highest(self):
        setattr(self, 'highest', True)
        return self


class Voter(models.Model):
    """
    Voter model class:
    - uuid: voters unique identifier.
    - emso: citizens unique number.
    - question: foreign key of the question this voter can vote on.
    """
    uuid = models.CharField(max_length=64, unique=True)
    emso = models.CharField(max_length=255, verbose_name='emšo')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
