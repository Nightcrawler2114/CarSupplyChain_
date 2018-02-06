from django.urls import path
from django.contrib.auth.decorators import permission_required
from . import views

app_name = 'dealership'

urlpatterns = [
    path('dealership/initiate_wholesale_deal/',
         permission_required('dealership.dealership_admin')(views.InitiateWholesaleDeal.as_view()),
         name='wholesale_deal'),
    path('dealership/retail_cars_list/',
         views.RetailCarsList.as_view(),
         name='retail_cars_list'),
    path('dealership/<int:pk>/update/',
         permission_required('dealership.dealership_admin')(views.RetailCarUpdate.as_view()),
         name='retail_car_update'),
    path('dealership/<int:pk>/delete/',
         permission_required('dealership.dealership_admin')(views.RetailCarDelete.as_view()),
         name='retail_car_delete'),
    path('dealership/retail_deals_list/',
         permission_required('dealership.dealership_admin')(views.RetailDealsList.as_view()),
         name='retail_deals_list'),
    path('dealership/wholesale_deals_list/',
         permission_required('dealership.dealership_admin')(views.WholesaleDealsList.as_view()),
         name='wholesale_deals_list'),
    path('dealership/retail_deal/<int:pk>/status/', views.AcceptRetailDeal.as_view(), name='retail_deal_status'),

]


