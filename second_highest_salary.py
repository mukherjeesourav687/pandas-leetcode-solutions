import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee["rank"] = employee["salary"].rank(
        method="dense",
        ascending=False
    )

    result = employee[
        employee["rank"] == 2
    ][["salary"]].head(1)

    if result.empty:
        return pd.DataFrame({
            "SecondHighestSalary": [None]
        })

    result.columns = ["SecondHighestSalary"]

    return result