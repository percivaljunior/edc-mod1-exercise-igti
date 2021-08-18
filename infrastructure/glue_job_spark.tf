resource "aws_glue_job" "GLUE_JOB_SPARK" {
    name     = "GLUE_JOB_SPARK"
    role_arn = "arn:aws:iam::449441604967:role/glue-s3-percival"

    command {
        script_location = "s3://terraform-state-igti-percival/emr-code/pyspark/job_spark_from_tf.py"
    }

    default_arguments = {
        "--job-language" = "spark"
    }
}