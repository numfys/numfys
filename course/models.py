from django.db import models
from os.path import basename

class Course(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(verbose_name="Beskrivende tekst for kurset")
    date = models.DateField()
    published = models.BooleanField(default=True)
    promo_image = models.ImageField(upload_to='course_images',
                                    verbose_name='Promo-bilde som vises øverst',
                                    blank=True)

    class Meta:
        ordering = ['-date']


class CourseFile(models.Model):
    # Note: Possible change in future:
    # upload_to with course name in path, this
    # requires Course to handle change in pathname
    # if renaming Course.
    file = models.FileField(upload_to='course_files')
    course = models.ForeignKey("Course",
                               on_delete=models.CASCADE,
                               related_name="file")

    @property
    def basename(self):
        return basename(self.file.name)
