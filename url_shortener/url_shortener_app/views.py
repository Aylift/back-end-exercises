import string
import random

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, redirect

from .models import ShortenedURL
from .serializers import ShortenedURLSerializer

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    while True:
        short_code = ''.join(random.choices(characters, k=length))
        if not ShortenedURL.objects.filter(short_code=short_code).exists():
            return short_code

class CreateShortURL(APIView):
    def post(self, request):
        serializer = ShortenedURLSerializer(data=request.data)
        if serializer.is_valid():
            original_url = serializer.validated_data['original_url']
            short_code = generate_short_code()
            shortened = ShortenedURL.objects.create(original_url=original_url, short_code=short_code)
            short_url = request.build_absolute_uri(f'/{short_code}/')
            return Response({'short_url': short_url}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RedirectToOriginal(APIView):
    def get(self, request, short_code):
        shortened = get_object_or_404(ShortenedURL, short_code=short_code)
        return redirect(shortened.original_url)
