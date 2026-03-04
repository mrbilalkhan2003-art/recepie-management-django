from django.core.mail import send_mail
from django.conf import settings







def send_email_to_client():
    subject = "This Email Is From Django Server"
    message = "This IS a test massage from Django server email"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["bk8288212@gmail.com"]
    send_mail(subject , message ,from_email , recipient_list)