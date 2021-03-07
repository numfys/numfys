from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.flatpages import views
from notebook.views import module_list, example_list, random_notebook, NotebookView
from course.views import CourseView, CourseListView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^modules/', module_list),
    url(r'^examples/', example_list),
    url(r'^search/', include('search.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^random/', random_notebook),
    url(r'^courses/$', CourseListView.as_view(), name="course_list"),
    url(r'^courses/(?P<pk>[\w-]+)/$', CourseView.as_view(), name="course"),
    url(r'^notebook/(?P<pk>[0-9]+)/$', NotebookView.as_view(), name="notebook"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# The pattern has to be at the end of the urlpatterns
urlpatterns += [
    url(r'^(?P<url>.*/)$', views.flatpage),
]
