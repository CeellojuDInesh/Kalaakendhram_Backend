from rest_framework import serializers
from .models import Category, Product, Variant, VariantImage


class VariantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariantImage
        fields = ["id", "image_url", "order"]


class VariantSerializer(serializers.ModelSerializer):
    images = VariantImageSerializer(many=True, read_only=True)

    class Meta:
        model = Variant
        fields = [
            "id",
            "label",
            "price",
            "image_url",   # optional fallback/single image
            "is_available",
            "images",      # 👈 new gallery list
        ]


class ProductSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "code",
            "description",
            "main_image",
            "is_active",
            "display_order",
            "variants",
        ]


class CategoryWithProductsSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "slug", "order", "products"]
