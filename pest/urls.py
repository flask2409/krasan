from django.conf.urls import url
from .views import pest_list, pest_detail, category, category_list

urlpatterns = [
	url(r'^product/(?P<id>\d+)/$', pest_detail, name = 'pest_show'),
   	url(r'^product/$', pest_list, name = 'pest_list'),
	url(r'^pest/$', category_list, name = 'pest_cat_list'),
    url(r'^pest/(?P<id>\d+)/$', category, name = 'pest_category'),
   
]
