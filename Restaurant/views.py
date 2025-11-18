from django.shortcuts import render 
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from .models import *
# Create your views here.
def index(request):
    items = menu.objects.all()
    context = {'items': items}
    return render(request, 'index.html', context)


# vistas de la api

class BookingView(viewsets.ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = bookingSerializer
    permission_classes = [IsAuthenticated]
    
class MenuItemView(generics.ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializer
