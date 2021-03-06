from django.contrib import admin

from .models import JournalEntry, WeightEntry, \
    TennisRacket, TennisString, TennisStringJob, \
    Author, Book, ReadingLog, BookStatus, BookStatusRef, \
    DietEntry


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


class BookStatusInline(admin.TabularInline):
    """ Creates inline (nested form). """
    extra = 0   # show no additional records for the inlines table. default = 3.
    model = BookStatus


class BookAdmin(admin.ModelAdmin):
    """ More customizable way to register models:
        Create a ModelAdmin class.
        Create rules / features for the class to use in /admin/.
        Register the model along with the ModelAdmin class.
    """
    # Configure list display:
    list_display = ('title', 'author')
    fields = ('title', 'author', 'total_pages', 'summary', 'review_url', 'library_url', 'isbn')

    # Adds the related model inline:
    inlines = [BookStatusInline]


class BookStatusAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'status_date', 'status')
    fields = ('user', 'book', 'status')


class BookStatusRefAdmin(admin.ModelAdmin):
    list_display = ('status', 'logical_order')
    fields = ('status', 'logical_order')


class DietEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'meal', 'created_date', 'score')
    fields = ('user', 'title', 'text', 'type','meal', 'score')


admin.site.register(JournalEntry)
admin.site.register(WeightEntry)
admin.site.register(TennisStringJob)
admin.site.register(TennisRacket, TennisRacketAdmin)
admin.site.register(TennisString, TennisStringAdmin)
admin.site.register(ReadingLog)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookStatus, BookStatusAdmin)
admin.site.register(BookStatusRef, BookStatusRefAdmin)
admin.site.register(DietEntry, DietEntryAdmin)