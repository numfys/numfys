# Generated by Django 3.1 on 2021-03-21 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_course_promo_image_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursefile',
            name='name',
            field=models.CharField(blank=True, help_text='Dersom det ikke er gitt et navn, brukes filnavnet.', max_length=60, verbose_name='Navn på fil'),
        ),
    ]
