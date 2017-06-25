from django.shortcuts import render
from .models import Category, Semena



def semena_list(request):
	semena = Semena.objects.all()
	return render(request, 'semena/list.html', {'semena':semena})


def semena_detail(request, id):
	semena = Semena.objects.get(id=id)
	return render(request, 'semena/detail.html', {'semena':semena})


def category(request, id):
	category = Category.objects.select_related().get(id=id)
	semena = category.semena_set.all()
	return render(request, 'semena/category.html', {'category':category, 'semena':semena})

def category_list(request):
	categories = Category.objects.all()
	return render(request, 'semena/category_list.html', {'categories':categories})


	
