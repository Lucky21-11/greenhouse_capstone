#ARYAN SHARMA 16015025070
import sci_calc

while True:
    print("\n--- Scientific Calculator ---")
    print("1. Power")
    print("2. Factorial")
    print("3. GCD")
    print("4. Prime Check")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            a = float(input("Enter base: "))
            b = float(input("Enter exponent: "))
            print("Result:", sci_calc.power(a, b))

        elif choice == 2:
            n = int(input("Enter a number: "))
            if n < 0:
                print("Factorial is not defined for negative numbers.")
            else:
                print("Factorial:", sci_calc.factorial(n))

        elif choice == 3:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("GCD:", sci_calc.gcd(a, b))

        elif choice == 4:
            n = int(input("Enter a number: "))
            if sci_calc.is_prime(n):
                print(n, "is a prime number.")
            else:
                print(n, "is not a prime number.")

        elif choice == 5:
            print("Exiting calculator...")
            break

        else:
            raise ValueError("Invalid menu choice!")

    except ValueError as e:
        print("Error:", e)
    except Exception as e:
        print("Something went wrong:", e)