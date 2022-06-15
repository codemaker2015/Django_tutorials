# Generated by Django 4.0.4 on 2022-05-05 07:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(blank=True, default='', max_length=200)),
                ('slug', models.SlugField(unique=True, verbose_name='Series slug')),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date published')),
            ],
            options={
                'verbose_name_plural': 'Series',
                'ordering': ['-published'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(blank=True, default='', max_length=200)),
                ('article_slug', models.SlugField(unique=True, verbose_name='Article slug')),
                ('content', models.TextField()),
                ('published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date published')),
                ('modified', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date modified')),
                ('series', models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.articleseries', verbose_name='Series')),
            ],
            options={
                'verbose_name_plural': 'Article',
                'ordering': ['-published'],
            },
        ),
    ]
