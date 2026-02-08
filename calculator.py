class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

def main(): # pragma: no cover
    calc = Calculator()
    print("=" * 60)
    print("~~ Simple Calculator ~~")
    print("=" * 60)
    print("Addition:", calc.add(5, 3))
    print("Subtraction:", calc.subtract(10, 4))
    print("Multiplication:", calc.multiply(6, 7))
    print("Division:", calc.divide(20, 4))
    print("=" * 60)
    
if __name__ == "__main__": # pragma: no cover
    main()