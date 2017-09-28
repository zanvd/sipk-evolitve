from django.conf.urls import url

from . import views

app_name = 'evolitve_app'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^question/(?P<pk>[0-9]+)/$', views.QuestionView.as_view(), name='question'),
    url(r'^question/(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^question/(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
