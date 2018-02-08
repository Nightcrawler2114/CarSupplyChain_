from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import WholesaleDeal, RetailCar, Dealership
from customer.models import RetailDeal, Customer


@method_decorator(login_required, name='dispatch')
class InitiateWholesaleDeal(CreateView):
    model = WholesaleDeal
    fields = ['manufacturer', 'car_name', 'total_price']
    success_url = '/'

    def form_valid(self, form):
        form.instance.initiated_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class RetailCarsList(ListView):
    model = RetailCar


@method_decorator(login_required, name='dispatch')
class RetailCarUpdate(UpdateView):
    model = RetailCar
    fields = ['name', 'price']
    success_url = '/dealership/retail_cars_list/'


@method_decorator(login_required, name='dispatch')
class RetailCarDelete(DeleteView):
    model = RetailCar
    success_url = '/dealership/retail_cars_list/'


@method_decorator(login_required, name='dispatch')
class RetailDealsList(ListView):
    model = RetailDeal
    template_name = 'dealership/retail_deals_list.html'


@method_decorator(login_required, name='dispatch')
class WholesaleDealsList(ListView):
    model = WholesaleDeal


@method_decorator(login_required, name='dispatch')
class AcceptRetailDeal(UpdateView):
    model = RetailDeal
    fields = ['status']
    success_url = '/dealership/retail_deals_list/'

    def form_valid(self, form):
        if form.instance.status == 'Y':
            customer = Customer.objects.get(user=form.instance.initiated_by)
            customer.balance = customer.balance - form.instance.total_price
            customer.save()
            dealership = Dealership.objects.get(name=form.instance.dealership.name)
            dealership.balance = dealership.balance + form.instance.total_price
            dealership.save()
        return super().form_valid(form)
