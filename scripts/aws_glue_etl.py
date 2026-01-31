"""
AWS Glue ETL Job: Bookings Data Processing
Purpose: Clean and transform bookings data from S3
"""

import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F
from pyspark.sql.types import DecimalType
from datetime import datetime

# ============================================
# Job Initialization
# ============================================

args = getResolvedOptions(sys.argv, [
    'JOB_NAME',
    'S3_BUCKET',
    'SOURCE_PREFIX',
    'TARGET_PREFIX'
])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# ============================================
# Configuration
# ============================================

S3_BUCKET = args['S3_BUCKET']
SOURCE_PREFIX = args['SOURCE_PREFIX']
TARGET_PREFIX = args['TARGET_PREFIX']

SOURCE_PATH = f"s3://{S3_BUCKET}/{SOURCE_PREFIX}/bookings.csv"
TARGET_PATH = f"s3://{S3_BUCKET}/{TARGET_PREFIX}/bookings/"

print(f"[INFO] Job started at: {datetime.now()}")
print(f"[INFO] Source: {SOURCE_PATH}")
print(f"[INFO] Target: {TARGET_PATH}")

# ============================================
# Read Data
# ============================================

print("[INFO] Reading source data...")

df = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .csv(SOURCE_PATH)

initial_count = df.count()
print(f"[INFO] Read {initial_count:,} records")
df.printSchema()

# ============================================
# Clean Data
# ============================================

# Drop rows with any null values
print("[INFO] Dropping null values...")
df_clean = df.dropna()
after_null = df_clean.count()
print(f"[INFO] After dropping nulls: {after_null:,} records (removed {initial_count - after_null:,})")

# Drop duplicates based on booking_id
print("[INFO] Dropping duplicates...")
df_dedup = df_clean.dropDuplicates(['booking_id'])
after_dedup = df_dedup.count()
print(f"[INFO] After dropping duplicates: {after_dedup:,} records (removed {after_null - after_dedup:,})")

# ============================================
# Add Calculated Columns
# ============================================

print("[INFO] Adding calculated columns...")

df_transformed = df_dedup \
    .withColumn('total_booking_amount',
        (F.col('nights_booked') * F.col('booking_amount')).cast(DecimalType(10, 2))) \
    .withColumn('additional_cost',
        (F.col('cleaning_fee') + F.col('service_fee')).cast(DecimalType(10, 2))) \
    .withColumn('total_cost',
        (F.col('nights_booked') * F.col('booking_amount') + F.col('cleaning_fee') + F.col('service_fee')).cast(DecimalType(10, 2))) \
    .withColumn('processed_at', F.current_timestamp())

# Show sample
print("[INFO] Sample output:")
df_transformed.select(
    'booking_id', 'nights_booked', 'booking_amount',
    'total_booking_amount', 'additional_cost', 'total_cost'
).show(5, truncate=False)

# ============================================
# Write Output
# ============================================

print("[INFO] Writing to Parquet...")

df_transformed.write \
    .mode('overwrite') \
    .parquet(TARGET_PATH)

final_count = df_transformed.count()

# ============================================
# Summary
# ============================================

print("JOB SUMMARY")
print(f"Records read:     {initial_count:,}")
print(f"After null drop:  {after_null:,}")
print(f"After dedup:      {after_dedup:,}")
print(f"Final output:     {final_count:,}")

print(f"[INFO] Job completed at: {datetime.now()}")
job.commit()
