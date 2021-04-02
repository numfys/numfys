from django.shortcuts import render
from django.views.generic import DetailView
from notebook.models import Notebook
import random

def module_list(request):
    notebooks = Notebook.objects.filter(topic__nb_type='M', published=1)
    return render(request, template_name='notebook/notebook_list.html',
                  context={'notebooks': notebooks}, )

def example_list(request):
    notebooks = Notebook.objects.filter(topic__nb_type='E', published=1)
    return render(request, template_name='notebook/notebook_list.html',
                  context={'notebooks': notebooks}, )

def random_notebook(request):
    notebooks = Notebook.objects.filter(published=1)
    randNotebook = None

    if len(notebooks) > 0:
        randIndex = random.randint(0, len(notebooks)-1)
        randNotebook = notebooks[randIndex]

    return render(request, template_name='notebook/notebook_list.html',
                  context={'notebooks': [randNotebook]})

class NotebookView(DetailView):
    model = Notebook
    object_name = "notebook"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        with open(self.object.get_or_create_html_file(), "r") as f:
            context["html"] = f.read()

        return context
