"""Download NASA POWER daily data and build g6_irrigation_data.csv.

Source: NASA POWER Daily Point API
Location: Kolhapur, Maharashtra (16.705 N, 74.243 E)
Period: 2022-01-01 through 2025-12-31
Parameters: PRECTOTCORR and GWETROOT, community AG
"""

from pathlib import Path
import requests
import pandas as pd

LATITUDE = 16.705
LONGITUDE = 74.243
START = "20220101"
END = "20251231"
OUTPUT = Path("g6_irrigation_data.csv")
API_URL = "https://power.larc.nasa.gov/api/temporal/daily/point"


def main():
    params = {
        "parameters": "PRECTOTCORR,GWETROOT",
        "community": "AG",
        "longitude": LONGITUDE,
        "latitude": LATITUDE,
        "start": START,
        "end": END,
        "format": "JSON",
        "time-standard": "UTC",
    }

    response = requests.get(API_URL, params=params, timeout=60)
    response.raise_for_status()
    payload = response.json()

    if "properties" not in payload or "parameter" not in payload["properties"]:
        raise RuntimeError(
            "NASA POWER response did not contain the expected parameter data. "
            f"Response keys: {list(payload.keys())}"
        )

    parameter_data = payload["properties"]["parameter"]
    required = {"PRECTOTCORR", "GWETROOT"}
    missing = required - set(parameter_data)
    if missing:
        raise RuntimeError(
            f"NASA POWER did not return required parameter(s): {sorted(missing)}. "
            "Do not substitute a different soil-moisture variable without team approval."
        )

    rain = pd.Series(parameter_data["PRECTOTCORR"], name="rain_mm")
    wetness = pd.Series(parameter_data["GWETROOT"], name="soil_wetness")
    df = pd.concat([rain, wetness], axis=1).rename_axis("date").reset_index()
    df["date"] = pd.to_datetime(df["date"], format="%Y%m%d", errors="raise")
    df["rain_mm"] = pd.to_numeric(df["rain_mm"], errors="coerce").replace(-999, pd.NA)
    df["soil_wetness"] = pd.to_numeric(df["soil_wetness"], errors="coerce").replace(-999, pd.NA)
    df = df.sort_values("date").drop_duplicates(subset="date", keep="first").reset_index(drop=True)

    expected_dates = pd.date_range("2022-01-01", "2025-12-31", freq="D")
    actual_dates = pd.DatetimeIndex(df["date"])
    if not actual_dates.equals(expected_dates):
        missing_dates = expected_dates.difference(actual_dates)
        extra_dates = actual_dates.difference(expected_dates)
        raise RuntimeError(
            "Date coverage is not exactly daily from 2022-01-01 to 2025-12-31. "
            f"Missing dates: {len(missing_dates)}; extra dates: {len(extra_dates)}. "
            "Inspect the NASA response before using the dataset."
        )

    invalid = df["rain_mm"].isna() | df["soil_wetness"].isna()
    if invalid.any():
        bad_dates = df.loc[invalid, "date"].dt.strftime("%Y-%m-%d").tolist()
        raise RuntimeError(
            f"Missing/sentinel rainfall or root-zone wetness on {len(bad_dates)} date(s): "
            f"{bad_dates[:10]}. No rows were silently removed; inspect these values first."
        )

    if (df["rain_mm"] < 0).any():
        raise RuntimeError("Negative rainfall values remain after sentinel handling; inspect the API data.")

    df["rain_cat"] = "None"
    df.loc[df["rain_mm"].ge(2.5) & df["rain_mm"].le(15.5), "rain_cat"] = "Light"
    df.loc[df["rain_mm"].gt(15.5), "rain_cat"] = "Heavy"

    q1 = df["soil_wetness"].quantile(1 / 3)
    q2 = df["soil_wetness"].quantile(2 / 3)
    if q1 >= q2:
        raise RuntimeError(
            f"Soil-wetness tertile thresholds are not distinct (q1={q1}, q2={q2}); "
            "do not force categories without reviewing the distribution."
        )

    df["soil_cat"] = "Wet"
    df.loc[df["soil_wetness"].le(q2), "soil_cat"] = "Moderate"
    df.loc[df["soil_wetness"].le(q1), "soil_cat"] = "Dry"

    next_date = df["date"].shift(-1)
    next_soil_cat = df["soil_cat"].shift(-1)
    valid_next_day = next_date.eq(df["date"] + pd.Timedelta(days=1))
    df["soil_next_dry"] = pd.NA
    df.loc[valid_next_day, "soil_next_dry"] = next_soil_cat[valid_next_day].eq("Dry").astype(int)

    df = df.loc[df["soil_next_dry"].notna(), [
        "date", "rain_mm", "soil_wetness", "rain_cat", "soil_cat", "soil_next_dry"
    ]].copy()
    df["date"] = df["date"].dt.strftime("%Y-%m-%d")
    df["soil_next_dry"] = df["soil_next_dry"].astype(int)
    df.to_csv(OUTPUT, index=False)

    print(f"Created: {OUTPUT.resolve()}")
    print(f"Rows: {len(df)}")
    print("Columns:", ", ".join(df.columns))
    print(f"Soil tertile thresholds: q1={q1:.8g}, q2={q2:.8g}")
    print("Rain category counts:")
    print(df["rain_cat"].value_counts().reindex(["None", "Light", "Heavy"], fill_value=0))
    print("Soil category counts:")
    print(df["soil_cat"].value_counts().reindex(["Dry", "Moderate", "Wet"], fill_value=0))
    print("Missing values by column:")
    print(df.isna().sum())
    print("\nFirst 5 rows:")
    print(df.head().to_string(index=False))


if __name__ == "__main__":
    main()
