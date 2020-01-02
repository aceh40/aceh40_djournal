from datetime import date
from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.


class JournalEntry(models.Model):
    """ Used to store entries made by user.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    entry_type = (
        ('wl', 'Weight log'),
        ('rl', 'Reading log'),
        ('hl', 'Habit log'),

        ('dr', 'Daily review'),
        ('wr', 'Weekly review'),

        ('bw', 'Body-weight workout'),
        ('sw', 'Swim workout'),

        ('ts', 'Tennis string job'),
        ('tp', 'Tennis machine practice'),
        ('th', 'Tennis hitting session'),
        ('tm', 'Tennis match'),

        ('dl', 'Diet log'),
    )

    type = models.CharField(choices=entry_type, blank=True, null=True, max_length=3, help_text='Journal entry type')

    def __str__(self):
        return f'Title: {self.title}, date: {self.created_date}'

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def get_date(self):
        getdate = date.fromtimestamp(self.created_date)
        return getdate

    class Meta:
        """ Meta data, in this case we instruct to order list views by due_back.
        """
        verbose_name = 'Journal Entry'
        verbose_name_plural = 'Journal Entries'
        ordering = ['-created_date']


class Weight(JournalEntry):
    """ To replace WeightEntry (eventually).
        Subclass of JournalEntry.
    """
    weight_lb = models.DecimalField(blank=False, null=False, verbose_name='Weight in lb',
                                    max_digits=5, decimal_places=2
                                    )

    def set_type(self):
        """ Set the type of the journal entry."""
        self.type = 'wl'
        self.save()


class WeightEntry(models.Model):
    """
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    weight = models.DecimalField(blank=False, null=False, verbose_name='Weight in lb', max_digits=5, decimal_places=2)
    note = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return f'Weight: {self.weight}, date: {self.created_date}'

    class Meta:
        """ Meta data, in this case we instruct to order list views by due_back.
        """
        ordering = ['-created_date']
        verbose_name = 'Weight Entry'
        verbose_name_plural = 'Weight Entries'


class TennisString(models.Model):
    """ List of tennis strings
    """
    make = models.CharField(max_length=20, help_text='Enter string maker.')
    model = models.CharField(max_length=20, help_text='Enter string model.')
    variation = models.CharField(default='', blank=True, max_length=100,
                                 help_text='Enter string model variation or generation.'
                                 )

    string_type = (
        ('g', 'Natural Gut'),
        ('p', 'Polyester'),
        ('m', 'Multifilament'),
        ('n', 'Nylon'),
    )
    string_gauge = (('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'))

    type = models.CharField(choices=string_type, max_length=1, help_text='Type of string')
    gauge = models.CharField(choices=string_gauge, max_length=2, help_text='Gauge of string')
    url = models.URLField(null=True, blank=True, help_text="Link to string's page on stringforum.net")

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.make} {self.model} {self.variation} ({self.gauge})'

    class Meta:
        """ Meta data, in this case we instruct to order list views by due_back.
        """
        ordering = ['make', 'model', 'variation', 'gauge']
        verbose_name = 'Tennis String'
        verbose_name_plural = 'Tennis Strings'


class TennisRacket(models.Model):
    """ List of tennis strings
    """
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=150)
    variation = models.CharField(default='', blank=True, max_length=150)
    head_size = models.IntegerField(null=True, blank=True, verbose_name='Head Size')
    length = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=4, verbose_name='Length')
    strung_weight = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=4)
    unstrung_weight = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=4)
    swing_weight = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=5)
    balance = models.CharField(null=True, blank=True, max_length=20, verbose_name='Balance')
    stiffness = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=5)
    beam_width = models.CharField(null=True, blank=True, max_length=20)
    main_strings = models.IntegerField(null=True, blank=True)
    cross_strings = models.IntegerField(null=True, blank=True)
    min_tension = models.IntegerField(null=True, blank=True, verbose_name='Minimum Tension')
    max_tension = models.IntegerField(null=True, blank=True, verbose_name='Maximum Tension')
    mains_skip = models.CharField(null=True, blank=True, max_length=20)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.make} {self.model} {self.variation}'

    class Meta:
        """ Meta data, in this case we instruct to order list views by due_back.
        """
        ordering = ('make', 'model', 'variation')
        verbose_name = 'Tennis Racket'
        verbose_name_plural = 'Tennis Rackets'


class TennisStringJob(JournalEntry):
    """ Journal Entry of body weight exercise.
    """
    racket = models.ForeignKey(TennisRacket, on_delete=models.SET_NULL, null=True)
    main_string_id = models.ForeignKey(TennisString,
                                       on_delete=models.SET_NULL,
                                       null=True,
                                       related_name='main_string_id'
                                       )
    main_tension = models.DecimalField(null=False, blank=False, decimal_places=1, max_digits=3)
    cross_string_id = models.ForeignKey(TennisString,
                                        on_delete=models.SET_NULL,
                                        null=True,
                                        related_name='cross_string_id'
                                        )
    cross_tension = models.DecimalField(null=False, blank=False, decimal_places=1, max_digits=3)

    class Meta:
        """ Meta data, in this case we instruct to order list views by due_back.
        """
        ordering = ['-created_date']
        verbose_name = 'Tennis Stringing Job'
        verbose_name_plural = 'Tennis Stringing Jobs'

    def set_type(self):
        """ Set the type of the journal entry."""
        self.type = 'ts'
        self.title = f'Racket String Job'
        self.text = f'I strung racket {self.racket} with {self.main_string_id} main string on {self.main_tension} lb. and cross string {self.cross_string_id} on {self.cross_tension} lb.'
        self.save()


class Author(models.Model):
    """ Enter authors"""
    first_name = models.CharField(max_length=150,verbose_name='First Name')
    last_name = models.CharField(max_length=150, verbose_name='Last Name')
    wiki_page = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ('last_name', 'first_name')
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    # def get_absolute_url(self):
    #     """Returns the url to access a particular author instance."""
    #     return reverse('catalog:author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    """ Enter books"""
    author = models.ForeignKey(Author, verbose_name='Author',
                               help_text='Select book author.',
                               null=True, blank=False,
                               on_delete=models.SET_NULL)
    title = models.CharField(max_length=250, verbose_name='Title',
                             help_text='Enter book title.')
    is_ebook = models.BooleanField(help_text='Is this an e-book?', null=False, blank=True, default=0)
    total_pages = models.IntegerField(null=True, blank=True, verbose_name='Total pages',
                                      help_text='Enter total number of pages.')
    summary = models.TextField(null=True, blank=True,
                               max_length=1000, verbose_name='Brief Summary',
                               help_text='Enter a brief description of the book')
    review_url = models.URLField(null=True, blank=True,
                                 verbose_name='Online review page',
                                 help_text='Enter book review web page.')
    library_url = models.URLField(null=True, blank=True,
                                  verbose_name='Library page',
                                  help_text='Enter library web page.')
    isbn_link = "https://en.wikipedia.org/wiki/International_Standard_Book_Number"
    isbn = models.CharField('ISBN', null=True, blank=True, max_length=13,
                            help_text=f'13 Character <a href="{isbn_link}">ISBN number</a>')

    class Meta:
        # ordering = ('authors', 'title')
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.title}'

    def get_current_status(self):
        return BookStatus.objects.filter(book=self).order_by('-status_date').first()


class BookStatusRef(models.Model):
    """ Lists the book status codes.
    """
    status = models.CharField(max_length=25,null=False, blank=False)
    logical_order = models.IntegerField(null=False, blank=False, unique=True,)

    class Meta:
        ordering = ('logical_order',)

    def __str__(self):
        return self.status


class BookStatus(models.Model):
    """ User specific book status (to read, read, etc.)
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, db_index=True)
    status_date = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    status = models.ForeignKey(BookStatusRef, on_delete=models.SET_NULL, null=True, db_index=True)

    class Meta:
        ordering = ('-status_date',)
        verbose_name = 'Book Status'
        verbose_name_plural = 'Book Statuses'


class ReadingLog(JournalEntry):
    """ Subclass of JournalEntry.
    """
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, db_index=True)
    page = models.IntegerField()

    def set_type(self):
        """ Set the type of the journal entry."""
        self.type = 'rl'
        self.save()

    def get_percent_completed(self):
        """ Calculate percent completed."""
        # ~TODO: See how you can calculate percentage. How do you access the total pages of the book?
        if self.book.total_pages:
            pc = 100 * float(self.page) / float(self.book.total_pages)
            return pc
        else:
            return None

    def set_type(self):
        """ Set the type of the journal entry."""
        self.type = 'rl'
        self.title = f'Reading Log: {self.book}'
        self.text = f'I am reading  {self.book} and reached page {self.page} of {self.book.total_pages}, and completed {self.get_percent_completed} percent.'
        self.save()


class DietEntry(JournalEntry):
    """ Subclass of JournalEntry.
    """
    meal_type = (('b', 'Breakfast'), ('l', 'Lunch'), ('d', 'dinner'), ('s', 'Snack'))
    score_type = ((True, 'Good'), (False, 'Bad'))

    meal = models.CharField(choices=meal_type, max_length=1, help_text="Type of meal")
    score = models.BooleanField(choices=score_type, help_text="Meal score or rating")

    def set_type(self):
        """ Set the type of journal entry."""
        self.type = 'dl'
        self.title = f'{self.meal} log.'
        self.save()

