from django.shortcuts import render
from .models import Pages


def page(request, id):
	pages = Pages.objects.get(pk=id)
	return render(request, 'pages/pages.html', {'pages':pages})

