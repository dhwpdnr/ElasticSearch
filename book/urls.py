from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import BookDocumentView

router = DefaultRouter()
books = router.register('books',
                        BookDocumentView,
                        basename='bookdocument')

urlpatterns = [
    url('', include(router.urls)),
]
