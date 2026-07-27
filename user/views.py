
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from user.models import ProductUser
from user.serializers import RegisterSerializer



class Register(CreateAPIView):
    serializer_class = RegisterSerializer

class ListUser(ListAPIView):
    queryset = ProductUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [IsAuthenticated]
