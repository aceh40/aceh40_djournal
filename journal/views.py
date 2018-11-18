from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView

from .models import JournalEntry


# Create your views here.

def home(request):
    return render(request, 'journal/home.html')


def journal_list(request):
    journal = JournalEntry.objects.all()
    return render (request, 'journal/journal_list.html', {'journal':journal})


class JournalList(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = JournalEntry
    template_name = 'journal/journal_list.html'
    context_object_name = 'journal'
    paginate_by = 10

    def get_queryset(self):
        """ Get journal entries by User. Order by due back desc. """
        return JournalEntry.objects.filter(user=self.request.user).order_by('-created_date')
        # return JournalEntry.objects.filter(user=self.request.user).order_by('-created_date')


class JournalEntryCreate(LoginRequiredMixin, CreateView):
    """ """
    model = JournalEntry
    fields = ['title', 'text']

    def form_valid(self, form):
        """ """
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse('journal:journal'))


