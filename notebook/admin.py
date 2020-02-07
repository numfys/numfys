from django.contrib import admin
from django.forms import ModelForm
from django.forms.widgets import FileInput
from django.db import models
from django.utils.html import format_html
from notebook.models import Notebook, NotebookImage, NotebookFile, Topic
from taggit.forms import TagField
from taggit_labels.widgets import LabelWidget as TaggitLabelWidget


class TopicAdmin(admin.ModelAdmin):
    """Information on what to display and how in topic admin page."""

    list_display = ['name', 'nb_type', 'index', ]
    list_filter = ['nb_type', ]
    search_fields = ['nb_type', 'name', ]

    fieldsets = (
        (None, {'fields': ('nb_type', 'index', 'name', )}
         ),
    )


class NotebookFileInline(admin.TabularInline):
    """Upload files in notebook admin page."""
    model = NotebookFile
    extra = 1
    formfield_overrides = {models.FileField: {'widget': FileInput}, }


class NotebookImageInline(admin.TabularInline):
    """Upload images in notebook admin page."""
    model = NotebookImage
    extra = 1
    # Remove 'Clear' checkbox in ordinary ImageField widget
    formfield_overrides = {models.ImageField: {'widget': FileInput}, }


class NotebookForm(ModelForm):
    """Custom model form with improved widget for TagField"""
    tags = TagField(widget=TaggitLabelWidget)

class NotebookAdmin(admin.ModelAdmin):
    """Information on what to display and how in notebook admin page."""

    form = NotebookForm

    # Attributes to list notebooks after. First attribute (title) becomes
    # the link to the specific notebook change page
    list_display = ['name', 'topic', 'index', 'edit_date', 'published', ]
    list_filter = ['topic__nb_type', 'topic', 'published', ]
    search_fields = ['name', 'published', 'topic__name', 'pub_date',
                     'edit_date', ]

    # Upload images in notebook admin page
    inlines = [NotebookImageInline, NotebookFileInline, ]

    # Possible actions to ticked notebooks, apart from deletion
    actions = ['make_published', 'make_unpublished']

    # Custom make_published action message
    def make_published(self, request, queryset):
        rows_updated = queryset.update(published=1)
        message_bit = "%s notebook(s)" % rows_updated
        self.message_user(request, "%s successfully marked as published."
                          % message_bit)

    # Custom make_unpublished action message
    def make_unpublished(self, request, queryset):
        rows_updated = queryset.update(published=0)
        message_bit = "%s notebook(s)" % rows_updated
        self.message_user(request, "%s successfully marked as \
            unpublished." % message_bit)

    # Text in action dropdown
    make_published.short_description = "Mark selected notebooks as\
                                        published"
    make_unpublished.short_description = "Mark selected notebooks as \
                                          unpublished"

    fieldsets = (
        (None, {'fields': ('topic', 'index', 'published', 'name',
                           'body', 'file_ipynb', 'tags', )
                }
         ),
    )

admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Topic, TopicAdmin)
