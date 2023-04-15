from django.urls import path
from rest_framework.routers import DefaultRouter

from .apis import ProductViewsets, ProductSearch, ProductDocumentViewSet

router = DefaultRouter()
router.register('product', ProductViewsets, basename='product')
router.register('product_document', ProductDocumentViewSet, basename='product-document')

urlpatterns = [
    path("product_search/<str:query>/", ProductSearch.as_view())
]

urlpatterns += router.urls
