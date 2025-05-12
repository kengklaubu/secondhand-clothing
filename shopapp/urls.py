# secondhand_clothing/urls.py
from django.contrib import admin
from django.urls import path
from shopapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add/', views.add_item, name='add_item'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
