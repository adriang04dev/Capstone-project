from django.shortcuts import render 
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, viewsets
from .models import *
# Create your views here.
def index(request):
    return render(request, 'index.html',{})


# vistas de la api

class BookingView(viewsets.ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = bookingSerializer
    
class MenuItemView(generics.ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializer
