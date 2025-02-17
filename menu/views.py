from rest_framework.views import APIView
from rest_framework.response import Response
from menu.models import FoodCategory, Food
from menu.serializers import FoodCategorySerializer
from django.db.models import Exists, OuterRef
from drf_spectacular.utils import extend_schema_view, extend_schema


@extend_schema_view(
    get=extend_schema(
        summary="Список категорий блюд с опубликованными блюдами",
        description="Возвращает список категорий, содержащих хотя бы одно опубликованное блюдо. Категории отсортированы по полю `order_id`.",
        responses={200: FoodCategorySerializer(many=True)},
    )
)
class FoodCategoryListView(APIView):
    """
    Возвращает список категорий блюд, содержащих опубликованные блюда.
    """
    def get(self, request):
        # Получаем категории, в которых есть опубликованные блюда
        categories = FoodCategory.objects.annotate(
            has_published_foods=Exists(
                Food.objects.filter(category=OuterRef('pk'), is_publish=True)
            )
        ).filter(has_published_foods=True).order_by('order_id')

        # Сериализуем отфильтрованные категории
        serializer = FoodCategorySerializer(categories, many=True)
        return Response(serializer.data)
