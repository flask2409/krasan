from django.conf.urls import url
from .views import semena_list, semena_detail, category, category_list

urlpatterns = [
	url(r'^product/(?P<id>\d+)/$', semena_detail, name = 'semena_show'),
   	url(r'^product/$', semena_list, name = 'semena_list'),
	url(r'^semena/$', category_list, name = 'semena_cat_list'),
    url(r'^semena/(?P<id>\d+)/$', category, name = 'semena_category'),
   
]
