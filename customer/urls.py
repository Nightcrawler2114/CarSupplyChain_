from django.urls import path
from django.contrib.auth.decorators import permission_required
from .views import InitiateRetailDeal, RetailDealsList, ChangeBalance

app_name = 'customer'

urlpatterns = [
    path('customer/initiate_retail_deal/',
         permission_required('customer.customer')(InitiateRetailDeal.as_view()),
         name='retail_deal'),
    path('customer/retail_deals_list/', RetailDealsList.as_view(), name='retail_deals_list'),
]