from django.db import transaction
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import  IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from order.models import Cart, CartItem, Order, OrderItem
from order.permissions import IsCartOwner, IsOrderOwner
from order.serializers import CartSerializers, CartItemSerializers, OrderSerializers, OrderItemSerializers
from rest_framework import status


class CartViews(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class =CartSerializers
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Cart.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


    @action(detail=True, methods=["post"])
    def clear(self, request, pk=None):
        cart =  self.get_object()
        if not cart.items.exists():
            return Response({"error": "Корзина уже очищена"}, status=status.HTTP_400_BAD_REQUEST)

        count = cart.items.count()
        cart.items.all().delete()
        return Response(
            {"message": f"Корзина очищена: {count}"}, status=status.HTTP_200_OK


        )



    @action(detail=True, methods=["post"])
    def checkout(self, request, pk=None):
        # Получаем корзину по id
        cart = self.get_object()

        # Проверяем, что корзина не пустая
        if not cart.items.exists():
            return Response({
                "error": "Корзина Пуста"
            }, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():


             # Создаём заказ
            order = Order.objects.create(
                owner=request.user

            )

            # Проходим по всем товарам в корзине
            for item in cart.items.all():
                product = item.product

                if product is None:
                    return Response({
                        "error": f"У CartItem {item.id} отсутствует продукт"
                    }, status=status.HTTP_400_BAD_REQUEST)

                # Проверяем, хватает ли товара на складе
                if product.stock < item.quantity:
                    return Response({
                        "error": f"Недостаточно товара: {
                        product.name}"
                    }, status=status.HTTP_400_BAD_REQUEST)


                # Создаём товар внутри заказа
                OrderItem.objects.create(
                   order=order,
                   product=product,
                   quantity = item.quantity,
                   price = product.price,
               )


            # Уменьшаем количество товара на складе
                product.stock -= item.quantity
                product.save()




            return Response({
                "message": "Заказ успешно создан",
                "order_od": order.id

            }, status=status.HTTP_201_CREATED)



class CartItemViews(ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class =CartItemSerializers
    permission_classes = (IsAuthenticated, IsCartOwner)

    def get_queryset(self):
        return CartItem.objects.filter(
            cart__owner=self.request.user
        )



class OrderViews(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class =OrderSerializers
    permission_classes = (IsAuthenticated,)
    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]

    filterset_fields = ["status"]
    ordering_fields = ["created_at"]

    def get_queryset(self):
        return Order.objects.filter(owner=self.request.user)
    @action(detail=True, methods=["post"])
    def cancel(self, request, pk=None):
        order = self.get_object()
        if order.status == Order.Status.CANCELLED:
            return Response({
                "message": f"Заказ уже оменён: {order.status}"
            }, status=status.HTTP_200_OK)


        if order.status in [
            Order.Status.SHIPPED,
            Order.Status.DELIVERED,
        ]:

            return Response({
                "error": f"Заказ с статусом {order.status} нельзя отменить:"

            }, status=status.HTTP_400_BAD_REQUEST)
        for item in order.items.all():
            product = item.product
            product.stock += item.quantity
            product.save()
        order.status = Order.Status.CANCELLED
        order.save()
        return Response(
        {
            "message": f"Заказ успешно отменён"
        }, status=status.HTTP_200_OK
        )

    @action(detail=True, methods=["post"])
    def pay(self, request, pk=None):
        order = self.get_object()

        if order.status != Order.Status.PENDING:
            return Response({"error": "Оплатить можно только заказ со статусом «Ожидает оплаты»."}, status=status.HTTP_400_BAD_REQUEST)

        order.status = Order.Status.PAID
        order.save()
        return Response({"message": "Заказ был успешно оплачен"}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"])
    def processing(self, request, pk=None):
        order = self.get_object()
        if order.status != Order.Status.PAID:
            return Response({"error": "Передать в обработку можно только оплаченный заказ."}, status=status.HTTP_400_BAD_REQUEST)

        order.status = Order.Status.PROCESSING
        order.save()
        return Response({"massage": "Заказ принят в обработку. "}, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"])
    def ship(self, request, pk=None):
        order = self.get_object()
        if order.status != Order.Status.PROCESSING:
            return Response({"message":
                            f"Отправить можно только заказ, который находится в статусе 'Обрабатывается"}, status=status.HTTP_400_BAD_REQUEST)

        order.status = Order.Status.SHIPPED
        order.save()
        return Response({
            "message": "Заказ успешно отправлен."
        }, status=status.HTTP_200_OK)
    @action(detail=True, methods=["post"])
    def deliver(self, request, pk=None):
        order = self.get_object()
        if order.status != Order.Status.SHIPPED:
            return Response({"message":"Доставить можно только заказ со статусом 'Отправлен'."}, status=status.HTTP_400_BAD_REQUEST)
        order.status = Order.Status.DELIVERED
        order.save()
        return Response({"message": "Заказ успешно доствлен"}, status=status.HTTP_200_OK)


class OrderItemViews(ReadOnlyModelViewSet):
    serializer_class = OrderItemSerializers
    permission_classes = (IsAuthenticated, IsOrderOwner)

    def get_queryset(self):
        return OrderItem.objects.filter(
            order__owner=self.request.user
        )



