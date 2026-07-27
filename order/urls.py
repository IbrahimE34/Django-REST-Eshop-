
from rest_framework.routers import DefaultRouter
from order.views import (
    CartViews,
    CartItemViews,
    OrderViews,
    OrderItemViews
)



router = DefaultRouter()
router.register(r'carts', CartViews, basename='cart')
router.register(r'cart-items', CartItemViews, basename='cart-items')
router.register(r'orders', OrderViews, basename='order')
router.register(r'order-items', OrderItemViews, basename='order-items')
urlpatterns = router.urls


