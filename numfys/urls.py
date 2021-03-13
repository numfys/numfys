from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.flatpages import views
from course.views import CourseView, CourseListView
from notebook.views import module_list, example_list, random_notebook, NotebookView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^modules/', module_list),
    url(r'^examples/', example_list),
    url(r'^search/', include('search.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^random/', random_notebook),
    path('courses/', CourseListView.as_view(), name="course_list"),
    path('courses/<int:pk>/', CourseView.as_view(), name="course"),
    path('notebook/<int:pk>/', NotebookView.as_view(), name="notebook"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# The pattern has to be at the end of the urlpatterns
urlpatterns += [
    url(r'^(?P<url>.*/)$', views.flatpage),
]
