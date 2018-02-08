from django.db import models
from django.contrib.auth.models import User
from manufacturing.models import WholesaleCar, Manufacturer


class Dealership(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    balance = models.IntegerField()

    def __str__(self):
        return self.name


class DealershipAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dealership = models.ForeignKey(Dealership, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ('dealership_admin', 'Dealership Admin Rights'),
        )

    def __str__(self):
        return self.user.username


class WholesaleDeal(models.Model):
    DEAL_STATUS = (
        ('Y', 'Accept'),
        ('N', 'Reject'),
        ('W', 'Waiting')
    )
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True, blank=True)
    car_name = models.ForeignKey(WholesaleCar, on_delete=models.SET_NULL, null=True, blank=True)
    car_amount = models.IntegerField(default=1)
    total_price = models.IntegerField()
    status = models.CharField(max_length=2, choices=DEAL_STATUS, default='W')
    initiated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.car_name.name


class RetailCar(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name


