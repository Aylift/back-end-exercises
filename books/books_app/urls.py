from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, check_availability


router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('books/<int:pk>/availability/', check_availability, name='book-availability'),
]
