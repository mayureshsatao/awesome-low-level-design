from time import sleep

from SystemDesign.Creational.Factory.Notification import Notification
from SystemDesign.Creational.Factory.NotificationFactory import NotificationFactory


class PushNotification(Notification):
    def __init__(self, device_token, title, body):
        self._device_token = device_token
        self._title = title
        self._body = body

    def validate(self) -> bool:
        return self._device_token and len(self._device_token) == 64 and self._title and self._body

    def send(self) -> bool:
        print('PushNotification: Send message - Device token: ' + self._device_token)
        sleep(2)
        return True


NotificationFactory.register('push', PushNotification)