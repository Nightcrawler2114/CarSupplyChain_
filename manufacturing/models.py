from django.db import models
from django.contrib.auth.models import User


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    balance = models.IntegerField()

    def __str__(self):
        return self.name


class Blueprint(models.Model):
    name = models.CharField(max_length=100)
    manufacturing_cost = models.IntegerField()

    def __str__(self):
        return self.name


class ManufacturingOrder(models.Model):
    car_count = models.IntegerField()
    blueprint = models.ForeignKey(Blueprint, on_delete=models.CASCADE)


class WholesaleCar(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    blueprint = models.ForeignKey(Blueprint, on_delete=models.CASCADE, null=True, blank=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class ManufacturerAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ('manufacturer_admin', 'Manufacturer Admin Rights'),
        )

    def __str__(self):
        return self.user.username


