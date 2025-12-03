from time import sleep

from SystemDesign.Creational.Factory.Notification import Notification
from SystemDesign.Creational.Factory.NotificationFactory import NotificationFactory


class EmailNotification(Notification):
    def __init__(self, recipient_email, subject, body):
        self._recipient_email = recipient_email
        self._subject = subject
        self._body = body

    def validate(self) -> bool:
        return self._recipient_email and '@' in self._recipient_email and '.' in self._recipient_email

    def send(self) -> bool:
        print('Sending email...')
        sleep(2)
        return True


NotificationFactory.register('email', EmailNotification)

