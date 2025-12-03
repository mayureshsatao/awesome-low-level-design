from typing import Any

from SystemDesign.Creational.Factory.Notification import Notification


class NotificationFactory:
    _registry: dict[str, type[Notification]] = {}

    @classmethod
    def register(cls, channel: str, notification_class: type[Notification]):
        cls._registry[channel] = notification_class

    @classmethod
    def create_notification(cls, channel: str, **kwargs: Any) -> Notification:
        print(f"Registry contents: {cls._registry}")
        if channel not in NotificationFactory._registry:
            raise Exception('Invalid channel')
        notification = cls._registry[channel](**kwargs)
        if not notification.validate():
            raise Exception('Invalid notification for {}'.format(channel))
        return notification
