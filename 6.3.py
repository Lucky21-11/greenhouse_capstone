#ARYAN SHARMA 16015025070
import convert_utils

while True:
    print("\n--- Unit Conversion ---")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")
    print("3. Kilograms to Pounds")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            km = float(input("Enter distance in kilometers: "))
            print("Miles:", convert_utils.km_to_miles(km))

        elif choice == 2:
            celsius = float(input("Enter temperature in Celsius: "))
            print("Fahrenheit:", convert_utils.celsius_to_fahrenheit(celsius))

        elif choice == 3:
            kg = float(input("Enter weight in kilograms: "))
            print("Pounds:", convert_utils.kg_to_pounds(kg))

        elif choice == 4:
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please select 1-4.")

    except ValueError:
        print("Invalid input! Please enter a valid number.")