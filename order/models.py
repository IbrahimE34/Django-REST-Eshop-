
from django.contrib.auth import get_user_model
from django.db import models

# Импортируем модель товара
from product.models import Product

# Получаем текущую модель пользователя
User = get_user_model()


# =========================
# КОРЗИНА ПОЛЬЗОВАТЕЛЯ
# =========================
class Cart(models.Model):

    # Владелец корзины
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE  # если удалить пользователя, удалится и корзина
    )

    # Дата создания корзины
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.owner}"


# =========================
# ТОВАР В КОРЗИНЕ
# =========================
class CartItem(models.Model):

    # К какой корзине относится товар
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name="items"
    )

    # Какой товар добавили
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    # Количество товара
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.product.name


# =========================
# ЗАКАЗ
# =========================
class Order(models.Model):

    # Возможные статусы заказа
    class Status(models.TextChoices):

        PAID = "paid", "Оплачено"

        # Заказ только создан
        PENDING = "pending", "Ожидает"

        # Магазин начал обработку
        PROCESSING = "processing", "Обрабатывается"

        # Заказ отправлен клиенту
        SHIPPED = "shipped", "Отправлен"

        # Клиент получил заказ
        DELIVERED = "delivered", "Доставлен"

        # Заказ отменён
        CANCELLED = "cancelled", "Отменён"

    # Покупатель
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    # SET_NULL нужен чтобы заказ не удалялся
    # если удалить пользователя

    # Текущий статус заказа
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

    # Когда заказ был создан
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"


# =========================
# ТОВАР В ЗАКАЗЕ
# =========================
class OrderItem(models.Model):

    # К какому заказу относится товар
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    # Какой товар был заказан
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    # Количество товара
    quantity = models.PositiveIntegerField(default=1)

    # Цена товара на момент покупки
    # нужна потому что цена товара может измениться
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.product} x {self.quantity}"