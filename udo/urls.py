from django.conf.urls import url
from .views import udo_list, udo_detail, category, category_list

urlpatterns = [
	url(r'^product/(?P<id>\d+)/$', udo_detail, name = 'udo_show'),
   	url(r'^product/$', udo_list, name = 'udo_list'),
	url(r'^udo/$', category_list, name = 'udo_cat_list'),
    url(r'^udo/(?P<id>\d+)/$', category, name = 'udo_category'),
   
]
