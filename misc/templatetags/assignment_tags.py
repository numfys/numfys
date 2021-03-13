from notebook.models import Notebook
from django import template

register = template.Library()


@register.simple_tag
def recent_uploads():
    """Return the last published notebooks as a list."""

    # Sort every published notebook by date to one list, save the last
    # few to another list and reverses the order
    objects = sorted(Notebook.objects.filter(published=1),
                     key=lambda object: object.pub_date)
    recent_objects = objects[-3:]
    recent_objects.reverse()

    return recent_objects
