from django import forms

from . import models


class StringJobForm(forms.ModelForm):
    """ Form to enter string job details
    """
    class Meta:
        model = models.TennisStringJob
        fields = ('racket', 'main_string_id', 'main_tension', 'cross_string_id', 'cross_tension', 'text', )