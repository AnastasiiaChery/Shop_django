from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from range.models import GoodsShopList

from range.serializer import ShopSerializer


class MyApiView(APIView):

    def get(self, *args, **kwargs):
        qs = GoodsShopList.objects.all()
        serializer = ShopSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
