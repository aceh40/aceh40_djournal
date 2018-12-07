from django.contrib import admin

from .models import JournalEntry, WeightEntry, TennisRacket, TennisStringJob, Author, Book, ReadingLog

admin.site.register(JournalEntry)
admin.site.register(WeightEntry)
# admin.site.register(TennisRacket)
# admin.site.register(TennisString)
admin.site.register(TennisStringJob)
admin.site.register(ReadingLog)


class TennisRacketAdmin(admin.ModelAdmin):
    """ More customizable way to register models:
        Create a ModelAdmin class.
        Create rules / features for the class to use in /admin/.
        Register the model along with the ModelAdmin class.
    """
    # Configure list display:
    list_display = ('make', 'model', 'variation')

    fieldsets = (
        (None, {
            'fields': ('make', 'model', 'variation')
        }),
        ('Dimensions', {
            'fields': ('head_size', 'length', 'stiffness', 'beam_width')
        }),
        ('Weight', {
            'fields': ('strung_weight', 'unstrung_weight', 'swing_weight', 'balance')
        }),
        ('Stringing Instructions', {
            'fields': ('main_strings', 'cross_strings', 'min_tension', 'max_tension', 'mains_skip')
        }),
    )


class TennisStringAdmin(admin.ModelAdmin):
    """ More customizable way to register models:
        Create a ModelAdmin class.
        Create rules / features for the class to use in /admin/.
        Register the model along with the ModelAdmin class.
    """
    # Configure list display:
    list_display = ('make', 'model', 'variation', 'type', 'gauge')
    fields = ('make', 'model', 'variation', 'type', 'gauge', 'url')


class AuthorAdmin(admin.ModelAdmin):
    """ More customizable way to register models:
        Create a ModelAdmin class.
        Create rules / features for the class to use in /admin/.
        Register the model along with the ModelAdmin class.
    """
    # Configure list display:
    list_display = ('first_name', 'last_name')
    fields = ('first_name', 'last_name', 'wiki_page')


class BookAdmin(admin.ModelAdmin):
    """ More customizable way to register models:
        Create a ModelAdmin class.
        Create rules / features for the class to use in /admin/.
        Register the model along with the ModelAdmin class.
    """
    # Configure list display:
    list_display = ('title', 'completed')
    fields = ('title', 'authors', 'total_pages', 'summary', 'review_url', 'library_url', 'isbn', 'completed')


admin.site.register(TennisRacket, TennisRacketAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
