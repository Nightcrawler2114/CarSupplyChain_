from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import RetailDeal, Customer


@method_decorator(login_required, name='dispatch')
class InitiateRetailDeal(CreateView):
    model = RetailDeal
    fields = ['dealership', 'car_name', 'total_price']
    success_url = '/'

    def form_valid(self, form):
        form.instance.initiated_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class RetailDealsList(ListView):
    model = RetailDeal


@method_decorator(login_required, name='dispatch')
class ChangeBalance(UpdateView):
    model = Customer
    fields = ['balance']
    success_url = '/'