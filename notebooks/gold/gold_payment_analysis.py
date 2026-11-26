from pyspark import pipelines as dp
from pyspark.sql import functions as F
from pyspark.sql.window import Window


@dp.materialized_view(
    name="gold_payment_analysis",
    comment="Payment mode-wise delivered orders and revenue analysis"
)
def gold_payment_analysis():

    df = spark.read.table("gold_delivered_orders")

    result = (
        df.groupBy("payment_mode")
        .agg(
            F.count("*").alias("total_delivered_orders"),
            F.sum(F.col("quantity").cast("double") * F.col("unit_price").cast("double")).alias("total_revenue"),
            F.round(
                F.avg(F.col("quantity").cast("double") * F.col("unit_price").cast("double")), 2
            ).alias("average_transaction_value")
        )
    )

    window = Window.orderBy(F.col("total_revenue").desc())

    return result.withColumn(
        "revenue_rank",
        F.dense_rank().over(window)
    )
