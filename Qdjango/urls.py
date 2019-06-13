from django.conf.urls import include, url
from django.contrib import admin
import index.urls as blog_url
from DjangoUeditor import urls as djud_urls
from django.conf import settings
 
urlpatterns = [
    url(r'^blog/',include(blog_url)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ueditor/',include(djud_urls)),
]
 
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)