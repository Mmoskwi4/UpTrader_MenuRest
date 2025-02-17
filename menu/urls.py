from django.urls import path
from menu.views import FoodCategoryListView

urlpatterns = [
    path('foods/', FoodCategoryListView.as_view(), name='food-list'),
]