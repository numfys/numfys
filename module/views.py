from django.views.generic import ListView, DetailView
from django.utils import timezone

from module.models import Module


class ModuleListView(ListView):
    """Generic Django display view. Relevant documentation at
    https://docs.djangoproject.com/en/dev/ref/class-based-views/generic-display/#listview
    """

    model = Module

    def get_context_data(self, **kwargs):
        context = super(ModuleListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ModuleDetailView(DetailView):

    model = Module

    def get_context_data(self, **kwargs):
        context = super(ModuleDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context