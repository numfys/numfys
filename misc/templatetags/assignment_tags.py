from module.models import Module
from example.models import Example
from itertools import chain
from django import template

register = template.Library()


# This template function is located in the module app dir because it has
# to be somewhere
@register.assignment_tag
def recent_uploads():
    """Returns the last four published objects
    (module, example or document) as a list.
    """
    # Sorts every module, example and doc by date to one list, saves the last
    # three to another list and reverses the order
    objects = sorted(
        chain(Module.objects.all(), Example.objects.all()),
        key=lambda object: object.pub_date)
    recent_objects = objects[-4:]
    recent_objects.reverse()

    # If object is module or example, strip of first four characters
    for object in recent_objects:
        if (object.__class__.__name__ == 'Module' or
                object.__class__.__name__ == 'Example'):
            object.title = object.title[4:]

    return recent_objects