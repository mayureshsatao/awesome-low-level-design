from SystemDesign.Behavioral.strategy.Payment import Payment

import time

class Cryptocurrency(Payment):
    def __init__(self, wallet_address):
        self._wallet_address = wallet_address
        self._processing_fee = 2.5

    def validate(self) -> bool:
        return True if self._wallet_address and len(self._wallet_address) == 42 and self._wallet_address[:2] == '0x' else False

    def calculate_fee(self, amount) -> float:
        return self._processing_fee

    def process_payment(self, amount) -> bool:
        time.sleep(2)
        print(f"Crypto Payment of ${amount} Successful")
        return True
