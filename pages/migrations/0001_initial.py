# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-30 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True, verbose_name='Заголовок')),
                ('key', models.CharField(max_length=60, verbose_name='Ключевые слова')),
                ('description', models.TextField(max_length=300, verbose_name='Контент')),
                ('image', models.ImageField(upload_to='media/pages', verbose_name='Изоброжение страницы')),
                ('img_content', models.ImageField(upload_to='media/pages/content', verbose_name='Изоброжение в контенте')),
            ],
            options={
                'verbose_name_plural': 'Страницы',
            },
        ),
    ]