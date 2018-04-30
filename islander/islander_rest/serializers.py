from rest_framework import serializers
from islander_rest.models import FoodCategory, Restaurant

class FoodCategorySerializer(serializers.ModelSerializer):
    restaurants = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )
    class Meta:
        model = FoodCategory
        fields = ('name', 'description', 'restaurants')

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'latitude', 'longitude', 'zoom', 'opens_at',
'closed_at', 'holiday_opens_at', 'holiday_closed_at')
