class SimpleProduct:
    def __init__(self, firstValue, secondValue):
        self.firstValue = firstValue
        self.secondValue = secondValue

    def calculate_product(self):
        result = self.firstValue * self.secondValue
        print(f"PROD = {result}")
        return f"PROD = {result}"
