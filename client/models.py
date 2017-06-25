#-*- coding: utf-8 -*-
from django.db import models

class Client(models.Model):
	name = models.CharField(max_length=50, verbose_name="Название")
	url = models.CharField(max_length=50, verbose_name="Ссылка")
	description = models.TextField(max_length=300, verbose_name="Текст")
	logo = models.ImageField(upload_to='media/client_logo', verbose_name="Изображение")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Наши клиенты"

		
