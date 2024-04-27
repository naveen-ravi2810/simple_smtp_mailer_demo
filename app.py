from simple_smtp_mailer import Mailer   # Easy module to send mails
from dotenv import load_dotenv
import time
import os

load_dotenv()


mail = Mailer(
    sender_email=os.environ.get("SENDER_EMAIL"),
    sender_password=os.environ.get("SENDER_PASSWORD"),
)

mail.send_mail(
    template_path="mail.html",                      # Required
    reciever_mail="naveen.cravi@gmail.com",         # Required 
    subject="Checking the working process",         # Required
    name="Naveen",                                  # Kwargs
    sender="test user",                             # Kwargs
    time=str(time.time()),                          # Kwargs
)
