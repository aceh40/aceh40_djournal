from datetime import date, datetime, timedelta

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView
from django.db.models import Avg, Max, Min, Count
from .forms import StringJobForm, ReadingLogForm
from .models import JournalEntry, WeightEntry, TennisRacket, TennisString, TennisStringJob, ReadingLog, Book, Author, DietEntry


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
    paginate_by = 15

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


@login_required
def weight_list_view(request):
    """ Lists all books in the db."""
    weight_list = WeightEntry.objects.filter(user=request.user, created_date__gte=datetime.now()-timedelta(days=60)).order_by('-created_date')
    avg_15_dec = WeightEntry.objects.filter(user=request.user, created_date__gte=datetime.now()-timedelta(days=15)).aggregate(Avg('weight'))["weight__avg"]
    avg_15 = "{:.2f}".format(avg_15_dec)
    max_15_dec = WeightEntry.objects.filter(user=request.user, created_date__gte=datetime.now()-timedelta(days=15)).aggregate(Max('weight'))["weight__max"]
    max_15 = "{:.2f}".format(max_15_dec)
    min_15_dec = WeightEntry.objects.filter(user=request.user, created_date__gte=datetime.now()-timedelta(days=15)).aggregate(Min('weight'))["weight__min"]
    min_15 = "{:.2f}".format(min_15_dec)
    count_15_dec = WeightEntry.objects.filter(user=request.user, created_date__gte=datetime.now()-timedelta(days=15)).aggregate(Count('weight'))["weight__count"]
    count_15 = "{:.0f}".format(count_15_dec)
    avg_60_dec = WeightEntry.objects.filter(user=request.user, created_date__gte=datetime.now()-timedelta(days=60)).aggregate(Avg('weight'))["weight__avg"]
    avg_60 = "{:.2f}".format(avg_60_dec)
    max_60_dec = WeightEntry.objects.filter(user=request.user, created_date__gte=datetime.now()-timedelta(days=60)).aggregate(Max('weight'))["weight__max"]
    max_60 = "{:.2f}".format(max_60_dec)
    min_60_dec = WeightEntry.objects.filter(user=request.user, created_date__gte=datetime.now()-timedelta(days=60)).aggregate(Min('weight'))["weight__min"]
    min_60 = "{:.2f}".format(min_60_dec)
    count_60_dec = WeightEntry.objects.filter(user=request.user, created_date__gte=datetime.now()-timedelta(days=60)).aggregate(Count('weight'))["weight__count"]
    count_60 = "{:.0f}".format(count_60_dec)
    avg_365_dec = WeightEntry.objects.filter(user=request.user, created_date__gte=datetime.now()-timedelta(days=365)).aggregate(Avg('weight'))["weight__avg"]
    avg_365 = "{:.2f}".format(avg_365_dec)
    max_365_dec = WeightEntry.objects.filter(user=request.user, created_date__gte=datetime.now()-timedelta(days=365)).aggregate(Max('weight'))["weight__max"]
    max_365 = "{:.2f}".format(max_365_dec)
    min_365_dec = WeightEntry.objects.filter(user=request.user, created_date__gte=datetime.now()-timedelta(days=365)).aggregate(Min('weight'))["weight__min"]
    min_365 = "{:.2f}".format(min_365_dec)
    count_365_dec = WeightEntry.objects.filter(user=request.user, created_date__gte=datetime.now()-timedelta(days=365)).aggregate(Count('weight'))["weight__count"]
    count_365 = "{:.0f}".format(count_365_dec)
    # diet_today = DietEntry.objects.filter(created_date__gte=datetime.now() - timedelta(days=7))
    return render(request, 'journal/weight_list.html', {'weight_list': weight_list,
                                                        'avg_15': avg_15,
                                                        'max_15': max_15,
                                                        'min_15': min_15,
                                                        'count_15': count_15,
                                                        'avg_60': avg_60,
                                                        'max_60': max_60,
                                                        'min_60': min_60,
                                                        'count_60': count_60,                                                        'avg_60': avg_60,
                                                        'avg_365': avg_365,
                                                        'max_365': max_365,
                                                        'min_365': min_365,
                                                        'count_365': count_365,
                                                        })
#
#
# class WeightList(LoginRequiredMixin, generic.ListView):
#     """
#     Generic class-based view listing books on loan to current user.
#     """
#     model = WeightEntry
#     template_name = 'journal/weight_list.html'
#     context_object_name = 'weight'
#     paginate_by = 25
#
#     def get_queryset(self):
#         """ Get journal entries by User. Order by due back desc. """
#         return WeightEntry.objects.filter(user=self.request.user).order_by('-created_date')
#         # return JournalEntry.objects.filter(user=self.request.user).order_by('-created_date')
#
#     def get_30day_stats(self):
#         """ Get descriptive stats for last 30 days """
#         avg_30 = WeightEntry.objects.All().aggregate(Avg('weight'))
#         # count_30 = WeightEntry.objects.All().aggregate(Count('weight'))
#         # max_30 = WeightEntry.objects.All().aggregate(Max('weight'))
#         # min_30 = WeightEntry.objects.All().aggregate(Min('weight'))
#         return avg_30


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
    paginate_by = 25
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
    paginate_by = 25
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
            obj.type = 'ts'
            obj.title = f'Racket stringing job.'
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
    paginate_by = 25

    def get_queryset(self):
        """ Get string job entries by User. Order by due back desc. """
        return TennisStringJob.objects.filter(user=self.request.user).order_by('-created_date')


@login_required
def reading_log(request):
    """ Log reading progress. Enter book, page reached, book status and notes.

    :param request:
    :return:
    """
    if request.method == 'POST':
        reading_form = ReadingLogForm(request.POST)
        if reading_form.is_valid():
            obj = reading_form.save(commit=False)
            obj.type = 'rl'
            page = request.POST["page"]
            book_title = Book.objects.get(id=request.POST["book"])
            obj.title = f'Read {book_title} to page {page}.'
            obj = reading_form.save(commit=False)
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect(reverse('journal:reading_log_list'))
    else:
        reading_form = ReadingLogForm()
        return render(request, 'journal/reading_log_entry.html', {'reading_form': reading_form})


class ReadingLogListView(LoginRequiredMixin, generic.ListView):
    """ List reading log information.
    """
    model = ReadingLog
    template_name = 'journal/reading_log_list.html'
    context_object_name = 'reading_list'
    paginate_by = 25

    def get_queryset(self):
        return ReadingLog.objects.filter(user=self.request.user).order_by('-created_date')


@login_required
def book_list_view(request):
    """ Lists all books in the db."""
    book_list = Book.objects.all()
    paginate_by = 25
    return render(request, 'journal/book_list.html', {'book_list': book_list})


class BookEntryCreate(LoginRequiredMixin, CreateView):
    """ """
    model = Book
    fields = ['title', 'author', 'is_ebook', 'total_pages',
              'review_url', 'library_url', 'isbn', 'summary']

    def form_valid(self, form):
        """ """
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse('journal:book_list'))


@login_required
def author_list_view(request):
    """ Lists all books in the db."""
    author_list = Author.objects.all()
    paginate_by = 25
    return render(request, 'journal/author_list.html', {'author_list': author_list})


class AuthorEntryCreate(LoginRequiredMixin, CreateView):
    """ """
    model = Author
    fields = ['first_name', 'last_name', 'wiki_page']

    def form_valid(self, form):
        """ """
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(reverse('journal:author_list'))


class DietEntryCreate(LoginRequiredMixin, CreateView):
    """ """
    model = DietEntry
    fields = ['meal', 'score', 'text']

    def form_valid(self, form):
        """ """
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.type = 'dl'
        obj.save()
        return HttpResponseRedirect(reverse('journal:diet_list'))

#~TODO: Make this view work, or paginate the view below.
class DietListView(LoginRequiredMixin, generic.ListView):
    """ List reading log information.
    """
    model = DietEntry
    template_name = 'journal/diet_list.html'
    context_object_name = 'diet_list'
    paginate_by = 25

    def get_queryset(self):
        return DietEntry.objects.filter(user=self.request.user).order_by('-created_date')


@login_required
def diet_list_view(request):
    """ Lists all books in the db."""
    diet_list = DietEntry.objects.all().order_by('-created_date')
    # diet_today = DietEntry.objects.filter(created_date__gte=datetime.now() - timedelta(days=7))
    return render(request, 'journal/diet_list.html', {'diet_list': diet_list})


@login_required
def daily_habit_view(request):
    """ Track whether habits are followed daily."""
    loop = [0,1,0]
    return render(request, 'journal/daily_habit_view.html',{'loop': loop})