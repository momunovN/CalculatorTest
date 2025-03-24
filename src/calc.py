class Calculator:

    def sum(self, a: float, b: float) -> float:

        return a + b

    def subtract(self, a: float, b: float) -> float:

        return a - b

    def multiply(self, a: float, b: float) -> float:

        return a * b if a != 0 else 1

    def divide(self, a: float, b: float) -> float:

        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b
