from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView

from .forms import StringJobForm
from .models import JournalEntry, WeightEntry, TennisRacket, TennisString, TennisStringJob


# Create your views here.

def home(request):
    return render(request, 'journal/home.html')


@login_required
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


class WeightList(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = WeightEntry
    template_name = 'journal/weight_list.html'
    context_object_name = 'weight'
    paginate_by = 10

    def get_queryset(self):
        """ Get journal entries by User. Order by due back desc. """
        return WeightEntry.objects.filter(user=self.request.user).order_by('-created_date')
        # return JournalEntry.objects.filter(user=self.request.user).order_by('-created_date')


class WeightEntryCreate(LoginRequiredMixin, CreateView):
    """ """
    model = WeightEntry
    fields = ['weight', 'note']

    def form_valid(self, form):
        """ """
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse('journal:weight'))


class TennisRacketList(LoginRequiredMixin, generic.ListView):
    """ Create generic list view on the Book model."""
    model = TennisRacket
    paginate_by = 10
    # Simple way to override default data:
    context_object_name = 'tennis_racket_list'    # your own name for the list as a template variable
    template_name = 'journal/tennis_racket_list.html'    # Specify your own template name/location

    def get_queryset(self):
        """Another way to override the query set. This one is more flexible..."""
        return TennisRacket.objects.all()     # Get 5 books containing the title war.


class TennisRacketDetail(LoginRequiredMixin, generic.DetailView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = TennisRacket


class TennisStringList(LoginRequiredMixin, generic.ListView):
    """ Create generic list view on the Book model."""
    model = TennisString
    paginate_by = 10
    # Simple way to override default data:
    context_object_name = 'tennis_string_list'    # your own name for the list as a template variable
    template_name = 'journal/tennis_string_list.html'    # Specify your own template name/location

    def get_queryset(self):
        """Another way to override the query set. This one is more flexible..."""
        return TennisString.objects.all()     # Get 5 books containing the title war.


class TennisStringDetail(LoginRequiredMixin, generic.DetailView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = TennisString


@login_required
def string_job(request):
    """ Log a string job. Enter racquet, string objects, tension and notes.

    :param request:
    :return:
    """
    if request.method == 'POST':
        form = StringJobForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect(reverse('journal:string_job_list'))
    else:
        form = StringJobForm()
        return render(request, 'journal/string_job.html', {'form': form})


class StringJobList(LoginRequiredMixin, generic.ListView):
    """ List view of user's string jobs.
    """
    model = TennisStringJob
    template_name = 'journal/string_job_list.html'
    context_object_name = 'string_job_list'
    paginate_by = 10

    def get_queryset(self):
        """ Get string job entries by User. Order by due back desc. """
        return TennisStringJob.objects.filter(user=self.request.user).order_by('-created_date')
