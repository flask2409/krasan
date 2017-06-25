from django.shortcuts import render
from .models import Category, Pest



def pest_list(request):
	pest = Pest.objects.all()
	return render(request, 'pest/list.html', {'pest':pest})


def pest_detail(request, id):
	pest = Pest.objects.get(id=id)
	return render(request, 'pest/detail.html', {'pest':pest})



def category(request, id):
	category = Category.objects.select_related().get(id=id)
	pest = category.pest_set.all()
	return render(request, 'pest/category.html', {'category':category, 'pest':pest})

def category_list(request):
	categories = Category.objects.all()
	return render(request, 'pest/category_list.html', {'categories':categories})