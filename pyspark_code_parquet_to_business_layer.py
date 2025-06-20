import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1749351382840 = glueContext.create_dynamic_frame.from_catalog(database="db_youtube-data-analytics-cleansed", table_name="raw_statistics", transformation_ctx="AWSGlueDataCatalog_node1749351382840")

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1749351333575 = glueContext.create_dynamic_frame.from_catalog(database="db_youtube-data-analytics-cleansed", table_name="cleaned_statistics_reference_data", transformation_ctx="AWSGlueDataCatalog_node1749351333575")

# Script generated for node Join
Join_node1749351499723 = Join.apply(frame1=AWSGlueDataCatalog_node1749351382840, frame2=AWSGlueDataCatalog_node1749351333575, keys1=["category_id"], keys2=["id"], transformation_ctx="Join_node1749351499723")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=Join_node1749351499723, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1749343046534", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1749351616238 = glueContext.getSink(path="s3://youtube-data-analytics-business-dev", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=["region", "category_id"], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1749351616238")
AmazonS3_node1749351616238.setCatalogInfo(catalogDatabase="youtube_data_analytics_business",catalogTableName="data_analytics_business")
AmazonS3_node1749351616238.setFormat("glueparquet", compression="snappy")
AmazonS3_node1749351616238.writeFrame(Join_node1749351499723)
job.commit()