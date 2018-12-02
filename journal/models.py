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
    created_date = models.DateTimeField(auto_now_add=True,null=False, blank=False)

    def __str__(self):
        return f'Title: {self.title}, date: {self.created_date}'

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    class Meta:
        """ Meta data, in this case we instruct to order list views by due_back.
        """
        ordering = ['-created_date']


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


class TennisString(models.Model):
    """ List of tennis strings
    """
    make = models.CharField(max_length=20, help_text='Enter string maker.')
    model = models.CharField(max_length=20, help_text='Enter string model.')
    variation = models.CharField(default='', blank=True, max_length=100, help_text='Enter string model variation or generation.')

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


class TennisRacket(models.Model):
    """ List of tennis strings
    """
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=150)
    variation = models.CharField(default='', blank=True, max_length=150)
    head_size = models.IntegerField(null=True, blank=True)
    length = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=4)
    strung_weight = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=4)
    unstrung_weight = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=4)
    swing_weight = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=5)
    balance = models.CharField(null=True, blank=True, max_length=20)
    stiffness = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=5)
    beam_width = models.CharField(null=True, blank=True, max_length=20)
    main_strings = models.IntegerField(null=True, blank=True)
    cross_strings = models.IntegerField(null=True, blank=True)
    min_tension = models.IntegerField(null=True, blank=True)
    max_tension = models.IntegerField(null=True, blank=True)
    mains_skip = models.CharField(null=True, blank=True, max_length=20)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.make} {self.model} {self.variation}'


class TennisStringJob(JournalEntry):
    """ Journal Entry of body weight exercise.
    """
    racket = models.ForeignKey(TennisRacket, on_delete=models.SET_NULL, null=True)
    main_string_id = models.ForeignKey(TennisString, on_delete=models.SET_NULL, null=True, related_name='main_string_id')
    main_tension = models.DecimalField(null=False, blank=False, decimal_places=1, max_digits=3)
    cross_string_id = models.ForeignKey(TennisString, on_delete=models.SET_NULL, null=True, related_name='cross_string_id')
    cross_tension = models.DecimalField(null=False, blank=False, decimal_places=1, max_digits=3)


