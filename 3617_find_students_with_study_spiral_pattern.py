import pandas as pd

def find_study_spiral_pattern(
    students: pd.DataFrame,
    study_sessions: pd.DataFrame
) -> pd.DataFrame:

    study_sessions = study_sessions.copy()
    study_sessions['session_date'] = pd.to_datetime(
        study_sessions['session_date']
    )

    ans = []

    for sid, g in study_sessions.groupby('student_id'):

        g = g.sort_values('session_date').reset_index(drop=True)
        n = len(g)

        best_cycle = 0
        best_hours = 0

        for k in range(3, n // 2 + 1):

            pattern = g['subject'].iloc[:k].tolist()

            if len(set(pattern)) != k:
                continue

            ok = True

            for i in range(min(2 * k, n)):
                if g.loc[i, 'subject'] != pattern[i % k]:
                    ok = False
                    break

            if not ok or n < 2 * k:
                continue

            m = 0
            while m < n and g.loc[m, 'subject'] == pattern[m % k]:
                m += 1

            gaps = g['session_date'].iloc[:m].diff().dt.days.fillna(1)

            if (gaps > 2).any():
                continue

            if m >= 2 * k:
                best_cycle = k
                best_hours = g['hours_studied'].iloc[:m].sum()

        if best_cycle:

            s = students[students['student_id'] == sid].iloc[0]

            ans.append([
                sid,
                s['student_name'],
                s['major'],
                best_cycle,
                round(best_hours, 1)
            ])

    return (
        pd.DataFrame(
            ans,
            columns=[
                'student_id',
                'student_name',
                'major',
                'cycle_length',
                'total_study_hours'
            ]
        )
        .sort_values(
            ['cycle_length', 'total_study_hours'],
            ascending=[False, False]
        )
        .reset_index(drop=True)
    )