from django.contrib import admin
from .models import Course, CourseFile

class FileInline(admin.StackedInline):
    model = CourseFile

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines=[FileInline]
