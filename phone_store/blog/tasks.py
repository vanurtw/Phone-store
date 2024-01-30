from celery import shared_task
from django.core.mail import send_mail


@shared_task
def share_post(sender_email, post_url):
    subject = 'Blog post'
    message = f'Our post was recommended to you. \n The post is at the link: {post_url}'
    mail_sent = send_mail(subject, message, 'vanuartw@mail.ru', [sender_email])
    return mail_sent
