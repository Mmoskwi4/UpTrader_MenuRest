from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Тестовые страницы для демонстрации меню
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('team/', TemplateView.as_view(template_name='team.html'), name='team'),
    path('careers/', TemplateView.as_view(template_name='careers.html'), name='careers'),
    path('services/web/', TemplateView.as_view(template_name='services_web.html'), name='services_web'),
    path('services/mobile/', TemplateView.as_view(template_name='services_mobile.html'), name='services_mobile'),
    path('services/design/', TemplateView.as_view(template_name='services_design.html'), name='services_design'),
    path('services/consulting/', TemplateView.as_view(template_name='services_consulting.html'), name='services_consulting'),
    path('portfolio/', TemplateView.as_view(template_name='portfolio.html'), name='portfolio'),
    path('blog/', TemplateView.as_view(template_name='blog.html'), name='blog'),
    path('blog/tech/', TemplateView.as_view(template_name='blog_tech.html'), name='blog_tech'),
    path('blog/design/', TemplateView.as_view(template_name='blog_design.html'), name='blog_design'),
    path('blog/marketing/', TemplateView.as_view(template_name='blog_marketing.html'), name='blog_marketing'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    
    # Для sidebar меню
    path('categories/programming/', TemplateView.as_view(template_name='categories_programming.html'), name='categories_programming'),
    path('categories/python/', TemplateView.as_view(template_name='categories_python.html'), name='categories_python'),
    path('categories/django/', TemplateView.as_view(template_name='categories_django.html'), name='categories_django'),
    path('categories/javascript/', TemplateView.as_view(template_name='categories_javascript.html'), name='categories_javascript'),
    path('categories/design/', TemplateView.as_view(template_name='categories_design.html'), name='categories_design'),
    path('categories/ui-ux/', TemplateView.as_view(template_name='categories_ui_ux.html'), name='categories_ui_ux'),
    path('categories/graphic-design/', TemplateView.as_view(template_name='categories_graphic_design.html'), name='categories_graphic_design'),
    path('categories/marketing/', TemplateView.as_view(template_name='categories_marketing.html'), name='categories_marketing'),
]