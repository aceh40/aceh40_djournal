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

]

