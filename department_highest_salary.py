import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(
        employee,
        department,
        left_on="departmentId",
        right_on="id"
    )

    merged["rank"] = merged.groupby("departmentId")["salary"].rank(
        method="dense",
        ascending=False
    )

    result = merged[
        merged["rank"] == 1
    ][["name_y", "name_x", "salary"]]

    result.columns = ["Department", "Employee", "Salary"]

    return result