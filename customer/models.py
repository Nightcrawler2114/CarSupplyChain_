from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from dealership.models import RetailCar, Dealership


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField()

    class Meta:
        permissions = (
            ('customer', 'Customer Rights'),
        )

    def __str__(self):
        return self.user.username


class RetailDeal(models.Model):
    DEAL_STATUS = (
        ('Y', 'Accept'),
        ('N', 'Reject'),
        ('W', 'Waiting')
    )
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE, null=True, blank=True)
    car_name = models.ForeignKey(RetailCar, on_delete=models.CASCADE)
    car_amount = models.IntegerField()
    total_price = models.IntegerField()
    status = models.CharField(max_length=2, choices=DEAL_STATUS, default='W')
    initiated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.car_name.name

