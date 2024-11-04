from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mailing_service.urls')),
    path('users/', include('users.urls', namespace='users')),
    path('clients/', include('clients.urls', namespace='clients')),
    path('message/', include('message.urls', namespace='message')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
