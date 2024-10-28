# Generated by Django 5.1.2 on 2024-10-28 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='название')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='lms/course/', verbose_name='превью')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': 'курс',
                'verbose_name_plural': 'курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='lms/lesson/', verbose_name='превью')),
                ('video_url', models.URLField(blank=True, null=True, verbose_name='ссылка на видео')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lms.course', verbose_name='курс')),
            ],
            options={
                'verbose_name': 'урок',
                'verbose_name_plural': 'уроки',
            },
        ),
    ]
