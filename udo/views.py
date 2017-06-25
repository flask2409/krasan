from django.shortcuts import render
from .models import Category, Udo



def udo_list(request):
	udo = Udo.objects.all()
	return render(request, 'udo/list.html', {'udo':udo})


def udo_detail(request, id):
	udo= Udo.objects.get(id=id)
	return render(request, 'udo/detail.html', {'udo':udo})



def category(request, id):
	category = Category.objects.select_related().get(id=id)
	udo = category.udo_set.all()
	return render(request, 'udo/category.html', {'category':category, 'udo':udo})

def category_list(request):
	categories = Category.objects.all()
	return render(request, 'udo/category_list.html', {'categories':categories})
