import time

from SystemDesign.Behavioral.strategy.Payment import Payment


class PayPal(Payment):
    def __init__(self, email):
        self._email = email
        self._processing_fee = 0.03

    def validate(self) -> bool:
        return True if self._email and '@' in self._email and '.' in self._email else False

    def calculate_fee(self, amount) -> float:
        return amount * self._processing_fee

    def process_payment(self, amount) -> bool:
        time.sleep(2)
        print(f"Paypal Payment of ${amount} Successful")
        return True
