from django.contrib import admin
from django.urls import path, include
from .views import teste_django
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', teste_django),
    path('', include('carbonoapp.urls')),
    path('', include('carbonoapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
