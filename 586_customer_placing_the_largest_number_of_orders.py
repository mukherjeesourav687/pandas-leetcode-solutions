import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return (
        orders.groupby("customer_number")
        .size()
        .reset_index(name="order_count")
        .sort_values("order_count", ascending=False)
        [["customer_number"]]
        .head(1)
    )