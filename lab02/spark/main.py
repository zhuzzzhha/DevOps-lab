#!/usr/bin/env python3
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count

def main():
    spark = SparkSession.builder \
        .appName("Airflow Spark Job") \
        .master("spark://spark-master:7077") \
        .config("spark.sql.adaptive.enabled", "true") \
        .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
        .getOrCreate()

    print("Spark Job Started")
    print(f"Spark version: {spark.version}")

    data = [
        ("Alice", 34, "Engineering"),
        ("Bob", 45, "Sales"),
        ("Catherine", 29, "Engineering"),
        ("David", 38, "Marketing"),
        ("Elena", 31, "Sales"),
        ("Frank", 42, "Engineering")
    ]
    
    df = spark.createDataFrame(data, ["Name", "Age", "Department"])
    
    print("Original DataFrame:")
    df.show()
    

if __name__ == "__main__":
    main()