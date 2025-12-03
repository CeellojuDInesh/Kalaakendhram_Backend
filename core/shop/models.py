from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)           # e.g. "Photo Frames"
    slug = models.SlugField(unique=True)              # e.g. "photo"
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
    )
    name = models.CharField(max_length=150)           # e.g. "Classic Mandala"
    code = models.CharField(max_length=50)            # e.g. "Classic Frame", "V"
    description = models.TextField(blank=True)
    main_image = models.URLField()                    # default/main image
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.name


class Variant(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="variants",
    )
    label = models.CharField(max_length=20)           # e.g. "A4", "5x7"
    price = models.PositiveIntegerField()
    image_url = models.URLField(blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product.name} – {self.label}"




class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
    )
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    main_image = models.URLField()   # common cover image
    is_active = models.BooleanField(default=True)
    display_order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["display_order", "id"]

    def __str__(self):
        return self.name


class Variant(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="variants",
    )
    label = models.CharField(max_length=20)   # e.g. "A4"
    price = models.PositiveIntegerField()
    image_url = models.URLField(blank=True)   # optional (can keep as fallback)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product.name} – {self.label}"


class VariantImage(models.Model):
    """
    Extra gallery images per variant (size).
    Example: A4 can have 2–4 detailed photos.
    """
    variant = models.ForeignKey(
        Variant,
        on_delete=models.CASCADE,
        related_name="images",
    )
    image_url = models.URLField()
    order = models.PositiveIntegerField(default=0)  # to control order in slider

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"Image for {self.variant} ({self.image_url})"
