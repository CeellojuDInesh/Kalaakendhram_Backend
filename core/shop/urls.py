from django.urls import path
from .views import CategoryWithProductsAPIView

urlpatterns = [
    path(
        "categories-with-products/",
        CategoryWithProductsAPIView.as_view(),
        name="categories-with-products",
    ),
]

