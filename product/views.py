
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from product.models import Product

from product.serializers import ProductSerializer


# Полный CRUD для проекта

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
    )

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    filterset_fields = ["category"]
    search_fields = ["name"]
    ordering_fields = ["price", "created_at"]
