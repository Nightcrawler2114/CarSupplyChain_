from django.urls import path
from django.contrib.auth.decorators import permission_required
from .views import HomeView,\
    BlueprintListView, \
    BlueprintEditView, \
    BlueprintDeleteView, \
    BlueprintCreateView, \
    ManufacturingOrderInitiation, \
    WholesaleCarsListView, \
    WholesaleCarEditView, \
    WholesaleCarDeleteView, \
    WholesaleDealsList, \
    AcceptDealView

app_name = 'manufacturing'

# permissions

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('manufacturing/blueprints/',
         permission_required('manufacturing.manufacturer_admin')(BlueprintListView.as_view()),
         name='blueprints_list'),
    path('manufacturing/blueprints/<int:pk>/edit/',
         permission_required('manufacturing.manufacturer_admin')(BlueprintEditView.as_view()),
         name='blueprint_edit'),
    path('manufacturing/blueprint/<int:pk>/delete/',
         permission_required('manufacturing.manufacturer_admin')(BlueprintDeleteView.as_view()),
         name='blueprint_delete'),
    path('manufacturing/blueprints/create/',
         permission_required('manufacturing.manufacturer_admin')(BlueprintCreateView.as_view()),
         name='blueprint_create'),
    path('manufacturing/manufacturing_order/',
         permission_required('manufacturing.manufacturer_admin')(ManufacturingOrderInitiation.as_view()),
         name='manufacturing_order'),
    path('manufacturing/wholesale_cars/',
         permission_required('manufacturing.manufacturer_admin')(WholesaleCarsListView.as_view()),
         name='wholesale_cars_list'),
    path('manufacturing/wholesale_cars/<int:pk>/edit/',
         permission_required('manufacturing.manufacturer_admin')(WholesaleCarEditView.as_view()),
         name='wholesale_car_edit'),
    path('manufacturing/wholesale_cars/<int:pk>/delete/',
         permission_required('manufacturing.manufacturer_admin')(WholesaleCarDeleteView.as_view()),
         name='wholesale_car_delete'),
    path('manufacturing/wholesale_deals/',
         permission_required('manufacturing.manufacturer_admin')(WholesaleDealsList.as_view()),
         name='wholesale_deals_list'),
    path('manufacturing/wholesale_deal/<int:pk>/status/',
         permission_required('manufacturing.manufacturer_admin')(AcceptDealView.as_view()),
         name='wholesale_deal_status'),
]