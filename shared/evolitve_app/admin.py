# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Answer, Question, Voter


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Datum', {'fields': ['start_date', 'close_date']}),
    ]
    inlines = [AnswerInline]
    list_display = ('question_text', 'start_date', 'close_date', 'get_total_answered')
    search_fields = ['question_text']
    list_filter = ['start_date', 'close_date']


class VoterAdmin(admin.ModelAdmin):
    fields = ['emso', 'question']
    search_fields = ['uuid', 'emso', 'question']
    list_filter = ['question']


admin.site.index_title = 'Prva stran'
admin.site.site_title = 'Evolitve Administracija'
admin.site.site_header = 'Evolitve Administracija'
admin.site.register(Question, QuestionAdmin)
admin.site.register(Voter, VoterAdmin)
