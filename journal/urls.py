from django.urls import path

from . import views

app_name = 'journal'

urlpatterns = [
    path('', views.home, name='home'),
    path('journal/', views.JournalList.as_view(), name='journal'),
    # path('journal/list/', views.journal_list, name='journal_list'),
    path('journal/entry/', views.JournalEntryCreate.as_view(), name='journal_entry'),
    path('weight/', views.WeightList.as_view(), name='weight'),
    path('weight/entry/', views.WeightEntryCreate.as_view(), name='weight_entry'),

    path('tennis_rackets/', views.TennisRacketList.as_view(), name='tennis_racket_list'),
    path('tennis_rackets/<int:pk>/', views.TennisRacketDetail.as_view(), name='tennis_racket'),
    path('tennis_strings/', views.TennisStringList.as_view(), name='tennis_string_list'),
    path('tennis_strings/<int:pk>/', views.TennisStringDetail.as_view(), name='tennis_string'),
    path('string_job/', views.string_job, name='string_job'),
    path('string_job_list/', views.StringJobList.as_view(), name='string_job_list'),

    path('reading/', views.ReadingLogListView.as_view(), name='reading_log_list'),
    path('reading/entry/', views.reading_log, name='reading_entry'),
    path('reading/books/', views.book_list_view, name='book_list'),
    path ('reading/books/entry/', views.BookEntryCreate.as_view(), name='book_entry'),
    path('reading/authors/', views.author_list_view, name='author_list'),
    path('reading/authors/entry/', views.AuthorEntryCreate.as_view(), name='author_entry')
]

