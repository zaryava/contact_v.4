from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import lastnamev, ContactCreate

urlpatterns = [
    path('', lastnamev, name='last_name'),
    path('contact/', ContactCreate.as_view(), name='contact_create'),
    path('index/', lastnamev, name='last_name'),

]

# включаем возможность обработки картинок
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)