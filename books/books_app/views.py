from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author']

@api_view(['GET'])
def check_availability(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        return Response({'available': book.is_available})
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=404)
