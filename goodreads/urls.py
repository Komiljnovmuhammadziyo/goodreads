from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from goodreads import settings
from goodreads.view import landing_page

urlpatterns = [
    path('', landing_page.as_view(), name='landing_page'),
    path('users/', include('user.url')),
    path('book/', include('book.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

