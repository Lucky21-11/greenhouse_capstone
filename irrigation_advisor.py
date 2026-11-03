#ARYAN SHARMA 16015025070

from datetime import datetime, timedelta


def calculate_water_requirement(soil_moisture, temperature):
    """
    Calculate Water Requirement Index (WRI).

    Replace the formula below with the exact formula
    given in the question if required.
    """
    wri = (100 - soil_moisture) + (temperature * 0.3441176471)
    return wri


def get_irrigation_status(wri):
    """Return irrigation recommendation based on WRI."""

    if wri < 20:
        return "No Irrigation Required"
    elif wri < 40:
        return "Low Irrigation"
    elif wri < 60:
        return "Moderate Irrigation"
    else:
        return "High Irrigation Required"


def calculate_next_irrigation_date(last_irrigation_date, interval):
    """Calculate the next irrigation date."""

    date = datetime.strptime(last_irrigation_date, "%Y-%m-%d")
    next_date = date + timedelta(days=interval)

    return next_date.strftime("%Y-%m-%d")


def calculate_days_remaining(next_irrigation_date):
    """Calculate days remaining from today until next irrigation."""

    next_date = datetime.strptime(
        next_irrigation_date, "%Y-%m-%d"
    ).date()

    today = datetime.today().date()

    return (next_date - today).days


def validate_soil_moisture(soil_moisture):
    """Validate soil moisture percentage."""

    if soil_moisture < 0 or soil_moisture > 100:
        return False

    return True


def validate_temperature(temperature):
    """Validate temperature."""

    if temperature < -50 or temperature > 70:
        return False

    return True


def validate_interval(interval):
    """Validate irrigation interval."""

    if interval <= 0:
        return False

    return True


def generate_irrigation_report(
    soil_moisture,
    temperature,
    last_irrigation_date,
    interval
):
    """Generate a complete irrigation report."""

    wri = calculate_water_requirement(
        soil_moisture,
        temperature
    )

    status = get_irrigation_status(wri)

    next_date = calculate_next_irrigation_date(
        last_irrigation_date,
        interval
    )

    days_remaining = calculate_days_remaining(next_date)

    report = {
        "Soil Moisture": soil_moisture,
        "Temperature": temperature,
        "Water Requirement Index": wri,
        "Irrigation Status": status,
        "Last Irrigation Date": last_irrigation_date,
        "Irrigation Interval": interval,
        "Next Irrigation Date": next_date,
        "Days Remaining": days_remaining
    }

    return report


if __name__ == "__main__":

    assert get_irrigation_status(10) == "No Irrigation Required"
    assert get_irrigation_status(30) == "Low Irrigation"
    assert get_irrigation_status(50) == "Moderate Irrigation"
    assert get_irrigation_status(70) == "High Irrigation Required"

    assert validate_soil_moisture(50) == True
    assert validate_soil_moisture(120) == False

    assert validate_interval(7) == True
    assert validate_interval(0) == False

    assert calculate_next_irrigation_date(
        "2026-08-01", 7
    ) == "2026-08-08"

    print("All self-tests passed!")