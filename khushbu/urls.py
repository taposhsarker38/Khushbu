from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_title ='Khushbu'
admin.site.index_title ='Welcome to Khushbu admin panel'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('index.urls')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
