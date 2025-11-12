Django Menu App
Django приложение для создания и управления древовидными меню.

Особенности
Древовидная структура меню

Поддержка нескольких меню на одной странице

Автоматическое определение активного пункта по URL

Редактирование через стандартную админку Django

Всего 1 SQL-запрос на отрисовку меню

Поддержка named URLs и прямых URL


Использование в шаблонах
html
```
<!-- Основное меню -->
<nav>
    {% load menu_tags %}
    {% draw_menu 'main_menu' %}
</nav>

<!-- Дополнительное меню -->
<aside>
    {% draw_menu 'sidebar_menu' %}
</aside>
```

Загрузка тестовых данных
bash
```
# С использованием fixtures
python manage.py loaddata menu_data.json

# Или через админку Django
# 1. Зайдите в админку (/admin/)
# 2. Перейдите в раздел "Menu items"
# 3. Добавьте пункты меню вручную согласно структуре выше
```

Пример urls.py для тестирования
python
```
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
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
]
```

Тестирование
После загрузки тестовых данных вы можете использовать меню в шаблонах:

html
```
<!-- Основное меню -->
{% load menu_tags %}
{% draw_menu 'main_menu' %}

<!-- Боковое меню -->
{% draw_menu 'sidebar_menu' %}
```