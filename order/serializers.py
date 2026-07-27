

from order.models import Cart, CartItem, Order, OrderItem


from rest_framework import serializers


# class UserMiniSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductUser
#         fields = ["id", "email"]

# Json ответ и настройка видемости и логике
class CartSerializers(serializers.ModelSerializer):
    # owner = UserMiniSerializer(read_only=True)
    owner = serializers.StringRelatedField()

    class Meta:
        model = Cart
        fields = ['id', 'owner', 'created_at',]

class CartItemSerializers(serializers.ModelSerializer):
    product_name = serializers.CharField(
        source="product.name",
        read_only=True
    )

    class Meta:
        model = CartItem
        fields = [
            "cart",
            "product",
            "product_name",
            "quantity"
        ]
class OrderSerializers(serializers.ModelSerializer):
    # owner = UserMiniSerializer(read_only=True)
    owner = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = ["id", "owner", "status", "created_at", ]

class OrderItemSerializers(serializers.ModelSerializer):
    product_name = serializers.CharField(
        source="product.name",
        read_only=True
    )

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "order",
            "product",
            "product_name",
            "quantity",
            "price"
        ]
