from rest_framework import serializers
from user_orders.serializers import OrderSerializer
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    class Meta:
        model = Customer
        fields = ['first_name','last_name', 'born_date','register_date', 'order']