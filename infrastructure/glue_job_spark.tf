resource "aws_glue_job" "glue_job_spark" {
  name     = "glue_job_spark"
  role_arn = "arn:aws:iam::449441604967:role/glue-s3-percival"

  command {
    script_location = "s3://datalake-percival-igti-tf/emr-code/pyspark/job_spark_from_tf.py"
  }
}