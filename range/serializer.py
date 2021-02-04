from rest_framework.serializers import ModelSerializer

from .models import GoodsShopList


class ShopSerializer(ModelSerializer):
    class Meta:
        model = GoodsShopList
        fields = '__all__'
