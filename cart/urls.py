from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_view, name='view'),
    path('add/<int:pk>/', views.add_to_cart, name='add'),
    path('remove/<int:pk>/', views.remove_from_cart, name='remove'),
    path('update/<int:pk>/', views.update_quantity, name='update'),
    path('checkout/', views.checkout, name='checkout'),
    path('success/<int:pk>/', views.order_success, name='success'),
]
