from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app.views import index, salary, area, last_vacancies, skills

urlpatterns = [
    path('admin/', admin.site.urls),
    path('salary/', salary),
    path('area/', area),
    path('skills/', skills),
    path('last-vacancies/', last_vacancies),
    path('', index)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
