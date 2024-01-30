from django.urls import path
from .views import *

urlpatterns = [
    path('', blog_home, name='blog_home'),
    path('details/<slug:slug>/', blog_details, name='blog_details'),

]
