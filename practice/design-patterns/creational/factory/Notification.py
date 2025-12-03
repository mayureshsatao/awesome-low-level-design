from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def validate(self) -> bool: pass

    @abstractmethod
    def send(self) -> bool: pass
