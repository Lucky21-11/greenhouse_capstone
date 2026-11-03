#ARYAN SHARMA 16015025070
import irrigation_advisor

from irrigation_advisor import (
    calculate_water_requirement,
    get_irrigation_status,
    calculate_next_irrigation_date,
    calculate_days_remaining,
    generate_irrigation_report,
    validate_soil_moisture,
    validate_temperature,
    validate_interval
)


print("======================================")
print("     SUGARCANE IRRIGATION ADVISOR")
print("======================================")

try:
    number_of_plots = int(input("\nEnter number of plots: "))

    if number_of_plots <= 0:
        raise ValueError("Number of plots must be greater than 0.")

    for plot in range(1, number_of_plots + 1):

        print("\n--------------------------------------")
        print("Plot", plot)
        print("--------------------------------------")

        soil_moisture = float(
            input("Enter Soil Moisture (%): ")
        )

        if not validate_soil_moisture(soil_moisture):
            print("Invalid soil moisture! Must be between 0 and 100.")
            continue

        temperature = float(
            input("Enter Temperature (°C): ")
        )

        if not validate_temperature(temperature):
            print("Invalid temperature!")
            continue


        last_date = input(
            "Enter Last Irrigation Date (YYYY-MM-DD): "
        )

  
        try:
            irrigation_advisor.datetime.strptime(
                last_date, "%Y-%m-%d"
            )
        except ValueError:
            print("Invalid date format!")
            continue

        interval = int(
            input("Enter Irrigation Interval (days): ")
        )

        if not validate_interval(interval):
            print("Invalid irrigation interval!")
            continue


        wri = calculate_water_requirement(
            soil_moisture,
            temperature
        )


        status = get_irrigation_status(wri)

        next_date = calculate_next_irrigation_date(
            last_date,
            interval
        )


        days_remaining = calculate_days_remaining(
            next_date
        )

        print("\n========== IRRIGATION REPORT ==========")

        print("Soil Moisture              :", soil_moisture, "%")
        print("Temperature                :", temperature, "°C")
        print("Water Requirement Index    :", format(wri, ".2f"))
        print("Irrigation Status          :", status)
        print("Last Irrigation Date       :", last_date)
        print("Irrigation Interval        :", interval, "days")
        print("Next Irrigation Date       :", next_date)

        if days_remaining > 0:
            print(
                "Days Remaining             :",
                days_remaining,
                "days"
            )
        elif days_remaining == 0:
            print("Days Remaining             : Irrigation is due today")
        else:
            print(
                "Days Remaining             :",
                abs(days_remaining),
                "days overdue"
            )

        print("=======================================")


except ValueError as e:
    print("\nError:", e)