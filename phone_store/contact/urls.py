from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60 * 15 )(ContactView.as_view()), name='contact'),
    path('thanks/', ThanksView.as_view(), name='thanks'),
]
