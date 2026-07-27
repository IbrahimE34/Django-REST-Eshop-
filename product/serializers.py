from rest_framework import serializers

from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "price",
            "description",
            "category",
            "characteristics",
            "created_at",
            "updated_at",
            "stock",
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]