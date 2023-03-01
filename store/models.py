from django.db import models
from django.conf import settings

# Create your models here.
CATEGORY_CHOICES  = (
    ("S", "shirt"),
    ("SW", "sport wear")
)

LABEL_CHOICES = (
    ("P", "primary"),
    ("S", "secondary"),
    ("T", "terialry")
)
class Item(models.Model):
    title = models.CharField(max_length=500)
    price = models.FloatField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3, default="S")
    label = models.CharField(choices=LABEL_CHOICES, max_length=2, default="S")
class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.item
    

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username;
