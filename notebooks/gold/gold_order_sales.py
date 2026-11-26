from pyspark import pipelines as dp
from pyspark.sql import functions as F


@dp.materialized_view(
    name="gold_order_summary",
    comment="Order status-wise summary"
)
def gold_order_summary():

    df = spark.read.table("silver_orders_typed")

    return (
        df.groupBy("order_status")
        .agg(
            F.count("*").alias("total_order_records"),
            F.sum("quantity").alias("total_quantity"),
            F.sum("order_amount").alias("total_order_amount")
        )
        .orderBy("order_status")
    )
