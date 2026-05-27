import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee["rank"] = employee["salary"].rank(
        method="dense",
        ascending=False
    )

    result = employee[
        employee["rank"] == N
    ][["salary"]].head(1)

    if result.empty:
        return pd.DataFrame({
            f"getNthHighestSalary({N})": [None]
        })

    result.columns = [
        f"getNthHighestSalary({N})"
    ]

    return result