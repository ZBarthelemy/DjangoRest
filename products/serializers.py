from rest_framework import serializers
from products.models import Product, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='product-highlight', format='html')

    class Meta:
        model = Product
        fields = ('url', 'id', 'highlight', 'owner',
                  'name', 'regular_price', 'listed_price',
                  'product_description',
                  'product_type', 'is_stocked', 'is_flash_sale',
                  'owner', 'linenos')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'products')