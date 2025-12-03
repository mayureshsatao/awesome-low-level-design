from typing import Optional

from SystemDesign.Behavioral.strategy.Payment import Payment


class PaymentProcessor:
    def __init__(self):
        self._strategy: Optional[Payment] = None

    def set_strategy(self, strategy: Payment):
        self._strategy = strategy

    def checkout(self, amount):
        if self._strategy is None:
            raise RuntimeError('Strategy is not set')
        if not self._strategy.validate():
            raise RuntimeError('Details are not valid is not valid')
        fees = self._strategy.calculate_fee(amount)
        self._strategy.process_payment(amount + fees)
