from django.urls import path

# from .views import
from range.views import MyApiView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MyApiView.as_view(), name='range')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
