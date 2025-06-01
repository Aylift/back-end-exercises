from django.urls import path
from .views import CreateShortURL, RedirectToOriginal


urlpatterns = [
    path('api/shorten/', CreateShortURL.as_view(), name='create_short_url'),
    path('<str:short_code>/', RedirectToOriginal.as_view(), name='redirect_to_original'),
]
