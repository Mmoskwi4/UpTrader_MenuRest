from django import template
from django.utils.safestring import mark_safe
from menu.models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag("menu/menu.html", takes_context=True)
def draw_menu(context, menu_name):
    try:
        menu_items = MenuItem.objects.filter(menu__name=menu_name).select_related(
            "parent"
        )
    except Menu.DoesNotExist:
        return {"menu_items": []}

    request = context["request"]
    current_url = request.path

    # Функция для построения дерева меня и определения активных пунктов
    def build_menu_tree(menu_items, parent=None, active_ancestors=None):
        if active_ancestors is None:
            active_ancestors = set()

        tree = []
        filtered_menu_items = [item for item in menu_items if item.parent == parent]

        for item in filtered_menu_items:
            is_active = current_url.startswith(item.get_url())

            if is_active:
                ancestor = item.parent
                while ancestor:
                    active_ancestors.add(ancestor)
                    ancestor = ancestor.parent

            # Получаем потомков *до* проверки is_expanded
            children = build_menu_tree(menu_items, item, active_ancestors)

            is_expanded = (
                is_active or item in active_ancestors or children
            )  #  Делаем проверку на существование children

            tree.append(
                {
                    "item": item,
                    "is_active": is_active,
                    "children": children,
                    "is_expanded": is_expanded,
                }
            )
        return tree

    menu_tree = build_menu_tree(list(menu_items))
    print(menu_tree)
    return {"menu_items": menu_tree}


@register.simple_tag(takes_context=True)
def recursive_menu_template(context, menu_items, expanded_slugs, current_path):
    print("recursive_menu_template called with:")
    print("  menu_items:", menu_items)
    print("  expanded_slugs:", expanded_slugs)
    print("  current_path:", current_path)
    output = "<ul>"
    for item in menu_items:
        is_expanded = item.slug in expanded_slugs

        if is_expanded:
            css_class = "expanded"
        else:
            css_class = "collapsed"

        output += f'<li class="{css_class}"><a href="{item.get_absolute_url()}">{item.title}</a>'

        # Получаем дочерние элементы и рекурсивно вызываем шаблон, если нужно
        children = MenuItem.objects.filter(parent=item)
        if children:
            if (
                is_expanded
            ):  # Только если текущий элемент развернут, разворачиваем его потомков
                output += recursive_menu_template(
                    context, children, expanded_slugs, current_path
                )
        output += "</li>"
    output += "</ul>"
    return mark_safe(output)


@register.inclusion_tag("menu/top_menu.html")
def top_menu(expanded_slugs):
    menu_items = MenuItem.objects.filter(parent=None)
    return {"menu_items": menu_items, "expanded_slugs": expanded_slugs}
