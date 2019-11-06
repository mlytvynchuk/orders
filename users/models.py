from django.db import models
from user_orders.models import Order
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    born_date = models.DateField()
    register_date = models.DateField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.first_name,self.last_name)