import pandas as pd


def joint_prob(df, soil, rain):
    """
    Calculate P(soil_cat = soil AND rain_cat = rain).

    Returns:
        (probability, count)
        probability is None if the DataFrame is empty.
    """
    total = len(df)

    if total == 0:
        return None, 0

    count = (
        (df["soil_cat"] == soil) &
        (df["rain_cat"] == rain)
    ).sum()

    return float(count / total), int(count)


def marginal_prob(df, col, value):
    """
    Calculate P(col = value).

    Returns:
        (probability, count)
        probability is None if the DataFrame is empty.
    """
    total = len(df)

    if total == 0:
        return None, 0

    count = (df[col] == value).sum()

    return float(count / total), int(count)


def conditional_prob(df, target, given):
    """
    Calculate P(target conditions | given conditions).

    target and given must be dictionaries, for example:
        target = {"soil_next_dry": 1}
        given = {"soil_cat": "Dry", "rain_cat": "None"}

    Returns:
        (probability, event_count, support_count)

        probability is None if support_count is zero.
        event_count counts rows matching target AND given.
        support_count counts rows matching given.
    """
    target_mask = pd.Series(True, index=df.index)
    given_mask = pd.Series(True, index=df.index)

    for col, value in target.items():
        target_mask &= df[col].eq(value)

    for col, value in given.items():
        given_mask &= df[col].eq(value)

    support_count = int(given_mask.sum())

    if support_count == 0:
        return None, 0, 0

    event_count = int((target_mask & given_mask).sum())
    probability = event_count / support_count

    return float(probability), event_count, support_count

import pandas as pd


def build_probability_tables(df):
    soil_order = ["Dry", "Moderate", "Wet"]
    rain_order = ["None", "Light", "Heavy"]

    # Count observations for each soil-rain combination
    counts = pd.crosstab(
        df["soil_cat"],
        df["rain_cat"]
    ).reindex(
        index=soil_order,
        columns=rain_order,
        fill_value=0
    )

    N = len(df)

    # Joint probability: P(S and R)
    joint = counts / N

    # Marginal probabilities
    marginal_soil = counts.sum(axis=1) / N
    marginal_rain = counts.sum(axis=0) / N

    # Conditional probabilities
    # Each column sums to 1: P(soil | rain)
    soil_given_rain = counts.div(
        counts.sum(axis=0),
        axis=1
    ).fillna(0)

    # Each row sums to 1: P(rain | soil)
    rain_given_soil = counts.div(
        counts.sum(axis=1),
        axis=0
    ).fillna(0)

    return {
        "counts": counts,
        "joint": joint,
        "marginal_soil": marginal_soil,
        "marginal_rain": marginal_rain,
        "soil_given_rain": soil_given_rain,
        "rain_given_soil": rain_given_soil
    }


if __name__ == "__main__":
    df = pd.read_csv(
        "g6_irrigation_data_fixed.csv",
        keep_default_na=False
    )

    tables = build_probability_tables(df)

    for name, table in tables.items():
        print(f"\n{name.upper()}")
        print(table.round(4))

    print("\nJoint probability sum:",
          tables["joint"].to_numpy().sum())

    print("\nP(Soil | Rain) column sums:")
    print(tables["soil_given_rain"].sum(axis=0).round(4))

    print("\nP(Rain | Soil) row sums:")
    print(tables["rain_given_soil"].sum(axis=1).round(4))

def dry_tomorrow_table(df, min_support=10):
    soil_order = ["Dry", "Moderate", "Wet"]
    rain_order = ["None", "Light", "Heavy"]

    results = []

    for soil in soil_order:
        for rain in rain_order:

            probability, event_count, n = conditional_prob(
                df,
                target={"soil_next_dry": 1},
                given={
                    "soil_cat": soil,
                    "rain_cat": rain
                }
            )

            if n == 0:
                status = "NO DATA"
            elif n < min_support:
                status = "LOW SUPPORT"
            else:
                status = "OK"

            results.append({
                "soil_cat": soil,
                "rain_cat": rain,
                "dry_tomorrow_count": event_count,
                "n": n,
                "p_dry_tomorrow": probability,
                "support_status": status
            })

    return pd.DataFrame(results)


if __name__ == "__main__":
    df = pd.read_csv(
        "g6_irrigation_data_fixed.csv",
        keep_default_na=False
    )
    df["soil_next_dry"] = pd.to_numeric(df["soil_next_dry"])

    result = dry_tomorrow_table(df)

    print(result.to_string(index=False))

def dry_tomorrow_by_soil(df):
    soil_order = ["Dry", "Moderate", "Wet"]
    results = []

    for soil in soil_order:
        probability, event_count, n = conditional_prob(
            df,
            target={"soil_next_dry": 1},
            given={"soil_cat": soil}
        )

        results.append({
            "soil_cat": soil,
            "dry_tomorrow_count": event_count,
            "n": n,
            "p_dry_tomorrow": probability
        })

    return pd.DataFrame(results)
