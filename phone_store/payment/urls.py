from django.urls import path
from .views import *

urlpatterns = [
    path('process/', process_payment, name='payment_process'),
    path('completed/', payment_completed, name='completed'),
    path('cancel/', payment_cancel, name='cancel'),

]