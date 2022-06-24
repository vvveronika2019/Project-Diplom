from rest_framework import serializers

from . models import Cart, Good, Goodcategory, Goodcounty
from . models import Goodparameter, Goodtheme, Review, Sell
from . models import Sellstatus, User, Sysdiagrams, Newscolibri


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = '__all__'

class GoodcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Goodcategory
        fields = '__all__'

class GoodcountySerializer(serializers.ModelSerializer):
    class Meta:
        model = Goodcounty
        fields = '__all__'

class GoodparameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goodparameter
        fields = '__all__'

class GoodthemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goodtheme
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class SellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell
        fields = '__all__'

class SellstatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sellstatus
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class SysdiagramsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sysdiagrams
        fields = '__all__'

class NewsColibriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newscolibri
        fields = '__all__'