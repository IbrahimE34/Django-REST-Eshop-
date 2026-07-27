from rest_framework.permissions import BasePermission


class IsCartOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.cart.owner == request.user

class IsOrderOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.order.owner == request.user