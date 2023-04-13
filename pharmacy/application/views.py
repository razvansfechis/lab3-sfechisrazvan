from django.shortcuts import render
from django.db.models import Avg

# Create your views here.

from rest_framework.views import APIView
from .models import Pharmacy, Customer, ProductDelivery
from .serializers import PharmacySerializers, CustomerSerializers, DeliverySerializers
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class PharmacyList(APIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializers

    def get(self, request, id=None):
        if id:
            pharmacy = Pharmacy.objects.get(id=id)
            serializer = PharmacySerializers(pharmacy)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        items = Pharmacy.objects.all()
        serializer = PharmacySerializers(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PharmacySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = Pharmacy.objects.get(id=id)
        serializer = PharmacySerializers(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=3):
        item = get_object_or_404(Pharmacy, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item deleted"}, status=status.HTTP_200_OK)

class CustomerList(APIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers

    def get(self, request, id=None):
        if id:
            customer = Customer.objects.get(id=id)
            serializer = CustomerSerializers(customer)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        items = Customer.objects.all()
        serializer = CustomerSerializers(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CustomerSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = Customer.objects.get(id=id)
        serializer = CustomerSerializers(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=3):
        item = get_object_or_404(Customer, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item deleted"}, status=status.HTTP_200_OK)


class DeliveryList(APIView):
    queryset = ProductDelivery.objects.all()
    serializer_class = DeliverySerializers

    def get(self, request, id=None):
        if id:
            delivery = ProductDelivery.objects.get(id=id)
            serializer = PharmacySerializers(delivery)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        items = ProductDelivery.objects.all()
        serializer = DeliverySerializers(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DeliverySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = ProductDelivery.objects.get(id=id)
        serializer = DeliverySerializers(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=3):
        item = get_object_or_404(ProductDelivery, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item deleted"}, status=status.HTTP_200_OK)

class StatisticsView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__stats = {
            1: self.__young_customers,
            2: self.__average_age
        }

    @staticmethod
    def __young_customers(request):
        customers = Customer.objects.all().order_by('age')

        response = {}
        for customer in customers:
            response[customer.age] = {
                "first_name": customer.first_name,
                "last_name": customer.last_name,
                "age": customer.age,
                "sex": customer.sex,
                "pharmacy": customer.pharmacy
            }

        return Response({"status": "success", "young_customers": response}, status=status.HTTP_200_OK)

    def get(self, request, id=None):
        if not id or id not in self.__stats:
            return Response({"status": "error", "available keys": self.__stats.keys()}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return self.__stats[id](request)
        
    @staticmethod
    def __average_age(request):
        age = Customer.objects.aggregate(Avg('age'))

        response = {
            "average age": age
        }

        return Response({"status": "success", "average_age": response}, status=status.HTTP_200_OK)

    def get(self, request, id=None):
        if not id or id not in self.__stats:
            return Response({"status": "error", "available keys": self.__stats.keys()}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return self.__stats[id](request)