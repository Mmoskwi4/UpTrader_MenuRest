from django.urls import path, include
from api.spectacular.urls import urlpatterns as doc_urls
from menu.urls import urlpatterns as menu_urls

app_name = "api"

urlpatterns = []

urlpatterns += doc_urls
urlpatterns += menu_urls
