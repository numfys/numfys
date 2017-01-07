# NumFys
A resource for use of numerical physics with <code>Python</code>, covering many topics in physics.

## Set up this web page on your system
1. Pull this repository
2. Use Python 3.5 and pip to install necessary packages and dependencies from `requirements.txt`, by running:

    ```
    pip install -r requirements.txt
    ```
NB! There might be a problem with the packages `libmysqlclient-dev` and `libjpeg8-dev` not being installed (problem detected on Ubuntu 16.04).
3. We recommend you use your own Django settings file, e.g. `devel.py`, when running the development server locally. This file will import `base.py`, overwrite certain variables in it and add some. It might look like this:
    ```python
    from .base import *
    import os

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    # Overwrite urls file for use in development
    ROOT_URLCONF = 'numfys.urls_devel'

    # Use a more light weight database than MySQL to develop locally
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    # Declare where "collectstatic" shall place static files
    STATIC_ROOT = os.path.join(BASE_DIR, '..', 'numfys_static')

    # To serve media files locally
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    ```
Every Django project has to have a `SECRET_KEY`, specific to each project, to be included in the `devel.py` or `production.py`. This is a 50 character string which you can create using the method that Django uses in `startproject` (taken from a discussion on [Stackoverflow](http://stackoverflow.com/questions/4664724/distributing-django-projects-with-unique-secret-keys)):
    ```python
    from django.utils.crypto import get_random_string
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    get_random_string(50, chars)
    ```
4. We also recommend that you use your own Django url file, e.g. `urls_devel.py`, when running the server locally. This is so that media files (e.g. Jupyter Notebooks as .html or .ipynb files, images etc.) are served by Django during development (see discusson in [Django's documentation](https://docs.djangoproject.com/en/1.9/howto/static-files/#serving-static-files-during-development). It might look like this:
    ```python
    from django.conf.urls import url, include
    from django.contrib import admin
    from django.views.generic import TemplateView
    from django.conf.urls.static import static
    from django.conf import settings


    urlpatterns = [
        url(r'^$', TemplateView.as_view(template_name='index.html')),
        url(r'^modules/', include('module.urls')),
        url(r'^admin/', admin.site.urls),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```
where the difference is in `+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`, which is not suited for production.
5. Set up the `SQLite` database by running the commands:

    ```
    ./manage.py makemigrations notebook
    ./manage.py migrate
    ```
6. We use `Bower` to manage front end packages like `Bootstrap` and `Font Awesome`. Install it, through their web site [bower.io](http://bower.io/), and `django-bower` with `pip install django-bower` (or `conda install django-bower`), as explained through their [GitHub page](https://github.com/nvbn/django-bower).
NB! There might be a problem with the package `libjpeg` not being installed (problem detected on Fedora 23 and Mint 17.3). If so, install this.
7. Time to run the Django development server. In the directory containing `manage.py`, run:

    ```
    ./manage.py runserver --settings=numfys.devel
    ```

---

Didn't work? Send us a message explaining what error message you got.

A project of the [Department of Physics](http://www.ntnu.edu/physics) at [NTNU](http://www.ntnu.edu/), supported by [Norgesuniversitetet](https://norgesuniversitetet.no).
