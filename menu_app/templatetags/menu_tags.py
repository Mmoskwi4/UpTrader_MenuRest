from django import template
from django.urls import resolve, Resolver404
from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('menu_app/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path_info
    
    try:
        resolved_url = resolve(current_url)
        current_named_url = resolved_url.url_name
    except Resolver404:
        current_named_url = None

    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')
    
    def build_tree(items, parent=None):
        tree = []
        for item in items:
            if item.parent == parent:
                children = build_tree(items, item)
                tree.append({
                    'item': item,
                    'children': children,
                    'is_active': False,
                    'is_expanded': False
                })
        return tree

    menu_tree = build_tree(menu_items)
    
    def find_and_mark_active(tree, current_path, current_named):
        active_found = False
        
        for node in tree:
            item = node['item']
            item_url = item.get_absolute_url()
            
            # Проверяем, является ли текущий пункт активным
            if (current_path == item_url or 
                (current_named and item.named_url == current_named)):
                node['is_active'] = True
                active_found = True
                # Разворачиваем текущий пункт и всех его детей первого уровня
                node['is_expanded'] = True
                
            # Рекурсивно проверяем детей
            child_active = find_and_mark_active(node['children'], current_path, current_named)
            if child_active:
                # Если найден активный ребенок, разворачиваем текущий пункт
                node['is_expanded'] = True
                active_found = True
                # НЕ разворачиваем всех детей, только отмечаем что нужно развернуть родителя
                
        return active_found
    
    find_and_mark_active(menu_tree, current_url, current_named_url)
    
    return {
        'menu_tree': menu_tree,
        'menu_name': menu_name
    }