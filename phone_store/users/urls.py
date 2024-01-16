from django.urls import path
from .views import register_user, logout_user

urlpatterns = [
    path('login/', register_user, name='login'),
    path('logout/', logout_user, name='logout'),

]
