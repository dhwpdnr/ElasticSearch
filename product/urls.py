from django.urls import path
from rest_framework.routers import DefaultRouter

from .apis import ProductViewsets, ProductSearch

router = DefaultRouter()
router.register('product', ProductViewsets, basename='product')

urlpatterns = [
    path("product_search/<str:query>/", ProductSearch.as_view())
]

urlpatterns += router.urls
