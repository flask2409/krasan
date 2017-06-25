#-*- coding: utf-8 -*-
from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=40, verbose_name = "Название категории")


	def __str__(self):
		return self.name


	class Meta:
		verbose_name_plural="Категории семян"



class Semena(models.Model):
	name = models.CharField(max_length=60, verbose_name="Название товара")
	text = models.TextField(max_length=2000, verbose_name="Описание")
	sort = models.CharField(max_length=300, verbose_name="Сорт", blank=True)
	image = models.FileField(upload_to='media/semana/price', verbose_name="Изображение", blank=True)
	file = models.FileField(upload_to='media/semena/price', verbose_name="Прайс лист", blank=True)
	category = models.ForeignKey(Category, verbose_name="Категория товара")

	def __str__(self):
		return self.name


	class Meta:
		verbose_name_plural = "Семена"
