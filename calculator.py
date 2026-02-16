import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Error! Cannot find square root of negative number."
    return math.sqrt(a)


def main():
    while True:
        print("\n====== ADVANCED CALCULATOR ======")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power")
        print("6. Square Root")
        print("7. Exit")

        choice = input("Choose operation (1-7): ")

        if choice in ["1", "2", "3", "4", "5"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    print("Result:", add(num1, num2))

                elif choice == "2":
                    print("Result:", subtract(num1, num2))

                elif choice == "3":
                    print("Result:", multiply(num1, num2))

                elif choice == "4":
                    print("Result:", divide(num1, num2))

                elif choice == "5":
                    print("Result:", power(num1, num2))

            except ValueError:
                print("Invalid input! Please enter numbers only.")

        elif choice == "6":
            try:
                num = float(input("Enter number: "))
                print("Result:", square_root(num))
            except ValueError:
                print("Invalid input!")

        elif choice == "7":
            print("Exiting Calculator. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
