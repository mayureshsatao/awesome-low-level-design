from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def validate(self) -> bool:
        pass

    @abstractmethod
    def calculate_fee(self, amount) -> float:
        pass

    @abstractmethod
    def process_payment(self, amount) -> bool:
        pass
