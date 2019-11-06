from django.db import models

class Order(models.Model):
    product = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product