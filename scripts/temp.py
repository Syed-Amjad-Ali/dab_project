from databricks.connect import DatabricksSession
#from pyspark.sql import SparkSession

spark = DatabricksSession.builder.remote(cluster_id ="0127-020851-itg45tig").getOrCreate()

spark.sql("SELECT 1").show()