import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [GLUE_JOB_SPARK]
args = getResolvedOptions(sys.argv, ['GLUE_JOB_SPARK'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['GLUE_JOB_SPARK'], args)

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