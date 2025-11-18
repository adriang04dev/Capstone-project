from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('' , views.index, name='index'),
    # Rutas de la api
    #path('api/bookings/', views.BookingView.as_view({'get': 'list'}), name='booking-list'),
    path('api/menu/', views.MenuItemView.as_view(), name='menu-list'),
    path('api/bookings/', views.BookingView.as_view({'get': 'list', 'post': 'create'}), name='booking-list'),
    path('api/menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]