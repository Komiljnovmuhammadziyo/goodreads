from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from goodreads import settings
from goodreads.view import landing_page, home_page

urlpatterns = [
    path('', landing_page.as_view(), name='landing_page'),
    path('home/', home_page.as_view(), name='home_page'),
    path('users/', include('user.urls')),
    path('book/', include('book.urls')),
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings. MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings. STATIC_URL, document_root=settings.STATICFILES_DIRS)

