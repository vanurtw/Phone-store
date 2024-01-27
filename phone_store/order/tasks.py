from celery import shared_task
from django.core.mail import send_mail


@shared_task
def order_created(order_email):
    subject = 'Order nr.'
    message = f'Order is processed.\n Thank you for choosing our store.'
    mail_sent = send_mail(subject, message, 'vanuartw@mail.ru', [order_email])
    return mail_sent
