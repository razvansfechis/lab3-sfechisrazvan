from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PharmacyList
from .views import CustomerList
from .views import DeliveryList
from .views import StatisticsView


urlpatterns = [
    path('pharm/', PharmacyList.as_view()),
    path('pharm/<int:id>/', PharmacyList.as_view()),

    path('customers/', CustomerList.as_view()),
    path('customer/<int:id>/', PharmacyList.as_view()),

    path('delivery/', DeliveryList.as_view()),
    path('delivery/<int:id>/', PharmacyList.as_view()),

    path('statistics/', StatisticsView.as_view()),
    path('statistics/<int:id>/', StatisticsView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
