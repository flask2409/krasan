from django.core.context_processors import request
from pages.models import Pages



def pages(request):
	pages = Pages.objects.all()
	return {'pages_all':pages} 


def page(request, id):
	pages = Pages.objects.get(pk=id)
	return render(request, 'pages/pages.html', {'pages':pages})

