from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Blueprint, ManufacturingOrder, Manufacturer, WholesaleCar, ManufacturerAdmin
from django.db import IntegrityError
from dealership.models import WholesaleDeal, RetailCar, Dealership


# Blueprints-related views
@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = 'template.html'


@method_decorator(login_required, name='dispatch')
class BlueprintListView(ListView):
    model = Blueprint


@method_decorator(login_required, name='dispatch')
class BlueprintEditView(UpdateView):
    model = Blueprint
    success_url = '/'
    fields = ['name', 'manufacturing_cost']


@method_decorator(login_required, name='dispatch')
class BlueprintDeleteView(DeleteView):
    model = Blueprint
    success_url = reverse_lazy('manufacturing:blueprints_list')


@method_decorator(login_required, name='dispatch')
class BlueprintCreateView(CreateView):
    model = Blueprint
    fields = ['name', 'manufacturing_cost']
    success_url = '/manufacturing/blueprints/'
    template_name_suffix = '_create_form'


# Manufacturing_order-related views
@method_decorator(login_required, name='dispatch')
class ManufacturingOrderInitiation(CreateView):
    model = ManufacturingOrder
    fields = ['car_count', 'blueprint']
    success_url = '/'

    def form_valid(self, form):
        count = 0
        while count < form.instance.car_count:
            WholesaleCar.objects.create(name=form.instance.blueprint.name)
            count += 1

        manufacturing_price = form.instance.car_count * form.instance.blueprint.manufacturing_cost
        current_manufacturer = Manufacturer.objects.get(name=self.request.user.manufactureradmin.manufacturer.name)
        current_manufacturer.balance = current_manufacturer.balance - manufacturing_price
        current_manufacturer.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class WholesaleCarsListView(ListView):
    model = WholesaleCar


@method_decorator(login_required, name='dispatch')
class WholesaleCarEditView(UpdateView):
    model = WholesaleCar
    success_url = '/wholesale_cars/'
    fields = ['name',]


@method_decorator(login_required, name='dispatch')
class WholesaleCarDeleteView(DeleteView):
    model = WholesaleCar
    success_url = reverse_lazy('manufacturing:wholesale_cars_list')


@method_decorator(login_required, name='dispatch')
class WholesaleDealsList(ListView):
    model = WholesaleDeal
    template_name = 'manufacturing/deals_list.html'


@method_decorator(login_required, name='dispatch')
class AcceptDealView(UpdateView):
    model = WholesaleDeal
    fields = ['status']
    success_url = '/manufacturing/wholesale_deals/'

    def form_valid(self, form):
        if form.instance.status == 'Y':
            count = 0
            while count < form.instance.car_amount:
                RetailCar.objects.create(name=form.instance.car_name.name)
                count += 1
            cars = WholesaleCar.objects.filter(name=form.instance.car_name.name)
            if len(cars) < 2:
                cars.delete()
            elif len(cars) > 1:
                cars[0].delete()
            current_manufacturer = Manufacturer.objects.get(name=self.request.user.manufactureradmin.manufacturer.name)
            current_manufacturer.balance = current_manufacturer.balance + form.instance.total_price
            current_manufacturer.save()
            dealership = Dealership.objects.get(name=form.instance.initiated_by.dealershipadmin.dealership.name)
            dealership.balance = dealership.balance - form.instance.total_price
            dealership.save()
        #     delete WholesaleCars
        return super().form_valid(form)

