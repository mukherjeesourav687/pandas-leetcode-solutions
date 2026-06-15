import pandas as pd

def students_and_examinations(
    students: pd.DataFrame,
    subjects: pd.DataFrame,
    examinations: pd.DataFrame
) -> pd.DataFrame:

    return (
        students.merge(subjects, how="cross")
        .merge(
            examinations.groupby(["student_id", "subject_name"])
            .size()
            .reset_index(name="attended_exams"),
            on=["student_id", "subject_name"],
            how="left"
        )
        .assign(
            attended_exams=lambda x: x["attended_exams"]
            .fillna(0)
            .astype(int)
        )
        .sort_values(["student_id", "subject_name"])
    )