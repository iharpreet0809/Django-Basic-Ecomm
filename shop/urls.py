from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from .views import product_list


router = DefaultRouter()
router.register(r'products', ProductViewSet)  # Registers API endpoints

urlpatterns = [
    path('', product_list, name='product_list'),  # Frontend product listing
    path('api/', include(router.urls)),  # API endpoints for CRUD operations
]
