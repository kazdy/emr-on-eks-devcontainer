from pyspark.sql import SparkSession

spark = SparkSession\
        .builder\
        .master('local')\
        .config("spark.submit.deployMode", "client")\
        .config("spark.hadoop.hive.metastore.client.factory.class","com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory")\
        .config("spark.hadoop.hive.metastore.glue.catalogid","XXXXXXXXXXX")\
        .config("spark.sql.catalogImplementation", "hive")\
        .appName("PythonPi")\
        .getOrCreate()
spark.sparkContext.setLogLevel("ERROR")      

sc = spark.sparkContext

jsonStr = ["""{ "metadata": { "key": 84896, "value": 54 }}"""]
# df = spark.read.json(sc.parallelize(jsonStr))
# df = spark.read.json("s3://blablablablabalbalbalbalbalablablaaaaa/example.json")

# df.show()
spark.sql('CREATE DATABASE IF NOT EXISTS customer_db;')
spark.sql("SHOW DATABASES").show()
spark.sql('SHOW TABLES;').show()
spark.sql('DESCRIBE TABLE poc_table').show()
