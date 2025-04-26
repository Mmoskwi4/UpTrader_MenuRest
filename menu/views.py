from django.shortcuts import get_object_or_404, render
from menu.models import MenuItem


def home(request):
    menu_items = MenuItem.objects.filter(parent=None)  # Только элементы верхнего уровня
    return render(request, "menu/home.html", {"menu_items": menu_items})


def menu_page(request, slug_path):
    slugs = slug_path.split("/")
    menu_item = get_object_or_404(MenuItem, slug=slugs[-1])
    children = MenuItem.objects.filter(parent=menu_item)  # Получаем потомков
    parent_url = menu_item.get_parent_url()

    # Формируем список slug для развернутых элементов
    expanded_slugs = slugs  # Все slug из URL должны быть развернуты

    return render(
        request,
        "menu/menu_page.html",
        {
            "menu_item": menu_item,
            "menu_items": children,
            "parent_url": parent_url,
            "expanded_slugs": expanded_slugs,  # Передаем список slug
        },
    )
