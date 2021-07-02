from django.urls import include, path
from . import views


from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [
path('', views.soryalist, name="home"),
path('addsoru/', views.createSoru, name="create_soru"),
path('soru/<str:pk_test>/', views.sorular, name="sorus"),
] + static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)