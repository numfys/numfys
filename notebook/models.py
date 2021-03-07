from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from nbconvert import HTMLExporter

from taggit.managers import TaggableManager
import os


class OverwriteStorage(FileSystemStorage):
    """Overwrite Django's storage function get_available_name to
    overwrite a new file's filename if it already exists.
    """

    def get_available_name(self, filename):
        if self.exists(filename):
            os.remove(os.path.join(settings.MEDIA_ROOT, filename))
        return filename


class Topic(models.Model):
    """Notebook topic database table attribute defitions."""
    NOTEBOOK_TYPE = (
        ('M', 'Module'),
        ('E', 'Example'),
    )
    nb_type = models.CharField(
        verbose_name='notebook type',
        max_length=1,
        choices=NOTEBOOK_TYPE,
        default='M',
    )
    name = models.CharField(
        verbose_name='topic name',
        max_length=50,
        help_text='Name of topic.',
        default='Basics',
    )
    index = models.IntegerField(
        help_text='Index of topic in topic list.',
        default=1,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['nb_type', 'index', ]


class Notebook(models.Model):
    """Notebook database table attribute defitions."""
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    index = models.IntegerField(
        help_text='Index of notebook in topic.',
        default=1,
    )
    published = models.BooleanField(
        # Default is published
        help_text='Untick to not display notebook on page.',
        default=1,
    )
    name = models.CharField(
        max_length=200,
        help_text='Name of notebook.',
        default='Notebook name',
    )
    pub_date = models.DateTimeField(
        verbose_name='date published',
        # Not shown in notebook admin page since auto_now_add
        auto_now_add=True,
        null=True,
    )
    edit_date = models.DateTimeField(
        # Not shown in notebook admin page since auto_now
        verbose_name='date edited',
        auto_now=True,
        null=True,
    )
    body = models.TextField(
        verbose_name='explanation',
        max_length=400,
        help_text='A short explanation of the notebook, max length of \
        400 signs including white spaces.',
        default='Notebook explanation',
    )
    file_ipynb = models.FileField(
        # Upload to media server
        verbose_name='.ipynb file',
        upload_to='notebooks',
        storage=OverwriteStorage(),
        null=True,
        help_text='Rendered using Jupyter\'s nbviewer.',
    )

    # From third party app 'django-taggit'
    # Docs: https://django-taggit.readthedocs.org/en/latest/index.html
    tags = TaggableManager(blank=True, )

    def clean(self):
        """Catch unwanted uploads and raise validation errors."""

        # File validation
        file_str = str(self.file_ipynb)
        if file_str[-5:] != 'ipynb':
            raise ValidationError(_('File error. You must upload the \
                notebook in the IPython Notebook format .ipynb.'))

    def __str__(self):
        """Identify notebook by name."""
        return self.name

    class Meta:
        ordering = ['topic__nb_type', 'topic__index', 'index']

    def to_html(self):
        exporter = HTMLExporter(template_name='classic')
        body, resources = exporter.from_file(self.file_ipynb.path)
        return body

class NotebookImage(models.Model):
    """Store media files used in notebooks on server."""
    notebook = models.ForeignKey(
        Notebook,
        related_name='images',
        on_delete=models.PROTECT
    )
    image = models.ImageField(
        blank=True,
        upload_to='notebooks/images',
        storage=OverwriteStorage(),
        help_text='Images in notebooks has to be included as \'images/file_name\'.',
    )

    def __str__(self):
        return self.image.name


class NotebookFile(models.Model):
    """Store arbitrary files used in notebooks on server."""
    notebook = models.ForeignKey(
        Notebook,
        related_name='files',
        on_delete=models.PROTECT
    )
    file = models.FileField(
        blank=True,
        upload_to='notebooks/files',
        storage=OverwriteStorage(),
        help_text='Files in notebooks has to be included as \'files/file_name\'.',
    )

    def __str__(self):
        return self.file.name
