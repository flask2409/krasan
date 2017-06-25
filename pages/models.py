#-*- coding: utf-8 -*-
from django.db import models

class Pages(models.Model):
	title = models.CharField(max_length=30, unique = True, verbose_name="Заголовок")
	key = models.CharField(max_length=60, verbose_name="Ключевые слова")
	description = models.TextField(max_length=1200, verbose_name="Контент")
	image = models.ImageField(upload_to='media/pages', verbose_name="Изоброжение страницы")
	img_content = models.ImageField(upload_to='media/pages/content', verbose_name="Изоброжение в контенте")


	def __str__(self):
		return self.title


	class Meta:
		verbose_name_plural="Страницы"
