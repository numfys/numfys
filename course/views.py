from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Course

class CourseView(DetailView):
    model = Course
    template_name = "course/course.html"

    def get_queryset(self):
        return super().get_queryset().filter(published=True)

class CourseListView(ListView):
    model = Course

    def get_queryset(self):
        return (
            super().get_queryset()
            .filter(published=True)
        )
