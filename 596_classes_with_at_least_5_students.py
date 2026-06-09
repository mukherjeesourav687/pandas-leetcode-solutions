import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    return (
        courses.groupby("class")
        .size()
        .reset_index(name="student_count")
        .query("student_count >= 5")[["class"]]
    )