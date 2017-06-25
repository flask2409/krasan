from django.conf.urls import url, include
from django.contrib import admin
from home.views import HomePage
from pages.views import page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomePage.as_view(), name = 'home'),
    url(r'^pages/(?P<id>\d+)/$', page, name = 'pages'),
    url(r'^semena/', include('semena.urls')),
    url(r'^pest/', include('pest.urls')),
    url(r'^udobreniya/', include('udo.urls')),
   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

