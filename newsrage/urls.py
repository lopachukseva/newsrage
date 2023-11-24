from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from news.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('news.urls')),
]

admin.site.site_header = 'Администрирование Newsrage'
admin.site.index_title = 'Администрирование сайта'
admin.site.site_title = 'Административный сайт Newsrage'

if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound
