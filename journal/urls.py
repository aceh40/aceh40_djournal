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
    path('string_job/', views.string_job, name='string_job'),
    path('string_job_list/', views.StringJobList.as_view(), name='string_job_list'),
]

