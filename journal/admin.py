from django.contrib import admin

from .models import JournalEntry, WeightEntry

admin.site.register(JournalEntry)
admin.site.register(WeightEntry)
