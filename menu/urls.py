from django.urls import path
import menu.views as menu_v

app_name = 'menu' # Namespace для именованных URL

urlpatterns = [
    path('menu/', menu_v.home, name='home'),
    path('menu/<path:slug_path>/', menu_v.menu_page, name='menu_page'),
]