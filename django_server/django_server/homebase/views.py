from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.serializers import Serializer

from .selectors import get_user, list_users

# Create your views here.


class UserDetail(APIView):
    def get(self, request, pk):
        data = get_user(pk)
        return Response(data=data, status=status.HTTP_200_OK)


class UserList(APIView):
    def get(self, request):
        data = list_users()
        return Response(data=data, status=status.HTTP_200_OK)
