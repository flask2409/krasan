from django.core.context_processors import request

from client.models import Client



def client(request):
	clients = Client.objects.all()[:7]
	return {'clients':clients} 