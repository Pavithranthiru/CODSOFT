class SimpleCalculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error! Division by zero."
        return x / y

    def get_numbers(self):
        try:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            return x, y
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            return None, None

    def display_menu(self):
        print("\nChoose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

    def run(self):
        print("Welcome to the Simple Calculator!")
        while True:
            self.display_menu()
            choice = input("Enter your choice (1/2/3/4/5): ")

            if choice == '5':
                print("Thank you for using the calculator! Goodbye!")
                break

            if choice in ['1', '2', '3', '4']:
                x, y = self.get_numbers()
                if x is None or y is None:
                    continue

                operations = {
                    '1': (self.add, "addition"),
                    '2': (self.subtract, "subtraction"),
                    '3': (self.multiply, "multiplication"),
                    '4': (self.divide, "division")
                }

                operation_func, operation_name = operations[choice]
                result = operation_func(x, y)
                print(f"The result of the {operation_name} is: {result}")
            else:
                print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    calculator = SimpleCalculator()
    calculator.run()
