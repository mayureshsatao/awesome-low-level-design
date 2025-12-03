import time
from datetime import datetime

from SystemDesign.Behavioral.strategy.Payment import Payment


class CreditCard(Payment):
    def __init__(self, credit_card_number, expiration_date):
        self._credit_card_number = credit_card_number
        self._expiration_date = expiration_date
        self._processing_fee = 0.025

    def validate(self) -> bool:
        month = int(self._expiration_date.split('/')[0])
        year = int(self._expiration_date.split('/')[1]) # expiry="12/25"
        return True if (len(self._credit_card_number) == 16 and
                        month >= datetime.now().month and year >= int(str(datetime.now().year)[2:])) else False

    def calculate_fee(self, amount) -> float:
        return self._processing_fee * amount

    def process_payment(self, amount) -> bool:
        time.sleep(2)
        print(f"Credit Card Payment of ${amount} Successful")
        return True
