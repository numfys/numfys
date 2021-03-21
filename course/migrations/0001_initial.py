# Generated by Django 3.1 on 2021-03-20 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(verbose_name='Beskrivende tekst for kurset')),
                ('date', models.DateField()),
                ('published', models.BooleanField(default=True)),
                ('promo_image', models.ImageField(blank=True, upload_to='course_images', verbose_name='Promo-bilde som vises øverst')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='CourseFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='course_files')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file', to='course.course')),
            ],
        ),
    ]
