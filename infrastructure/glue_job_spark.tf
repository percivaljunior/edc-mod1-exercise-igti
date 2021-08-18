resource "aws_glue_job" "glue_job_spark" {
  name     = "glue_job_spark"
  role_arn = aws_iam_role.glue_role.arn

  command {
    script_location = "s3://datalake-percival-igti-tf/emr-code/pyspark/job_spark_from_tf.py"
  }
}