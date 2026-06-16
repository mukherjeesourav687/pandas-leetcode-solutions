import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    reports_count = (
        employee.groupby("managerId")
        .size()
        .reset_index(name="cnt")
    )

    managers = reports_count[reports_count["cnt"] >= 5]

    return (
        employee.merge(
            managers,
            left_on="id",
            right_on="managerId"
        )[["name"]]
    )