from dataclasses import fields
from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ["address", "positions"]

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        for item in positions:
            new_stok_product = StockProduct.objects.create(product=item['product'], stock=stock,
                                                           quantity=item['quantity'],  price=item['price']
                                                           )
            stock.positions.add(new_stok_product)
        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)
        for item in positions:
            StockProduct.objects.update_or_create(defaults={'quantity': item['quantity'], 'price': item['price']},
                                                  product=item['product'], stock=stock
                                                  )
        return stock
