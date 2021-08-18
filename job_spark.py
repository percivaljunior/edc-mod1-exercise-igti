from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.appName("ExerciseSpark")
    .getOrCreate()
)

# Ler os dados do censo escolar 2020
censo = (
    spark
    .read
    .format("csv")
    .option("header", True)
    .option("inferSchema", True)
    .option("delimiter", "|")
    .load("s3://terraform-state-igti-percival/raw-data/censo-escolar/")
)
(
    censo
    .write
    .mode("overwrite")
    .format("parquet")
    .partitionBy("year")
    .save("s3://datalake-percival-igti-tf/staging/censo-escolar/")
)