from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from mainapp.models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

class SuvlarAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        suvlar=Suv.objects.all()
        serializer=SuvSerializer(suvlar, many=True)
        return Response(serializer.data)
    def post(self, request):
        suv=request.data
        serializer=SuvSerializer(data=suv)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class SuvAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        suv=Suv.objects.get(id=pk)
        serializer = SuvSerializer(suv)
        return Response(serializer.data)
    def put(self, request, pk):
        suv=Suv.objects.get(id=pk)
        serializer=SuvSerializer(suv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    def delete(self, request, pk):
        mahsulot=Suv.objects.get(id=pk)
        mahsulot.delete()
        return Response({"Success": "True"})

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class MijozlarAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        mijozlar=Mijoz.objects.filter()
        serializer=MijozSerializer(mijozlar, many=True)
        return Response(serializer.data)
    def post(self, request):
        mijoz=request.data
        serializer=MijozSerializer(data=mijoz)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)

class MijozAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        mijoz=Mijoz.objects.get(id=pk)
        serializer = MijozSerializer(mijoz)
        return Response(serializer.data)
    def put(self, request, pk):
        mijoz=Mijoz.objects.get(id=pk)
        if mijoz.user==request.user:
            serializer=MijozSerializer(mijoz, data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response({"xabar": "Bu mijoz bu userga tegishli emas!"})
    def delete(self, request, pk):
        mijoz=Mijoz.objects.get(id=pk)
        if mijoz.user==request.user:
            mijoz.delete()
            return Response({"Success": "True"})
        return Response({"xabar": "Bu mijoz bu userga tegishli emas!"})

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class BuyurtmalarAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        mahsulotlar=Buyurtma.objects.filter(admin__user=request.user)|Buyurtma.objects.filter(mijoz__user=request.user)
        serializer=BuyurtmaSerializer(mahsulotlar, many=True)
        return Response(serializer.data)
    def post(self, request):
        mahsulot=request.data
        serializer=BuyurtmaSerializer(data=mahsulot)
        if serializer.is_valid():
            serializer.save(mijoz=Mijoz.objects.get(user=request.user))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class AdminlarAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        mahsulotlar=Admin.objects.all()
        serializer=AdminSerializer(mahsulotlar, many=True)
        return Response(serializer.data)

class AdminAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        admin=Admin.objects.get(id=pk)
        ser=AdminSerializer(admin)
        return Response(ser.data)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class HaydovchilarAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        mahsulotlar = Haydovchi.objects.all()
        serializer = HaydovchiSerializer(mahsulotlar, many=True)
        return Response(serializer.data)


class HaydovchiAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        haydovchi = Haydovchi.objects.get(id=pk)
        ser = HaydovchiSerializer(haydovchi)
        return Response(ser.data)

