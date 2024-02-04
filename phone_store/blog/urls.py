from django.urls import path
from .views import *

urlpatterns = [
    path('', blog_home, name='blog_home'),
    path('details/<slug:slug>/', BlogPostDetail.as_view(), name='blog_details'),

]
