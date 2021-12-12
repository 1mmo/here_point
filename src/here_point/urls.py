from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache
from django.conf.urls.static import static


urlpatterns = [
    path('captcha/', include('captcha.urls')),
    path('accounts/', include('users.urls')),
    path('', include('main.urls')),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
    # Route for processing uploaded files
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)
