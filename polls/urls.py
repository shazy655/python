from django.urls import path

from . import views

from polls.views import AboutView
from polls.book import BookListView

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('about/', AboutView.as_view()),
    path('books/', BookListView.as_view()),

]