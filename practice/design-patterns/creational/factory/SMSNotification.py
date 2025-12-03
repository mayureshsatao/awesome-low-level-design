from time import sleep

from SystemDesign.Creational.Factory.Notification import Notification
from SystemDesign.Creational.Factory.NotificationFactory import NotificationFactory


class SMSNotification(Notification):
    def __init__(self, phone_number, message):
        self._message = message
        self._phone_number = phone_number

    def validate(self) -> bool:
        return self._phone_number and len(self._phone_number) == 10 and self._message and len(self._message) < 160

    def send(self) -> bool:
        print('SMSNotification: Send message - Phone number: ' + str(self._phone_number))
        sleep(2)
        return True


NotificationFactory.register('sms', SMSNotification)