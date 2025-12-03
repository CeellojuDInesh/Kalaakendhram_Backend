from django.contrib import admin
from .models import Category, Product, Variant, VariantImage


class VariantImageInline(admin.TabularInline):
    model = VariantImage
    extra = 1


class VariantInline(admin.TabularInline):
    model = Variant
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "is_active")
    list_filter = ("category", "is_active")
    inlines = [VariantInline]  # gallery is per variant, so inline there


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "order")


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    list_display = ("product", "label", "price", "is_available")
    list_filter = ("product", "is_available")
    inlines = [VariantImageInline]
