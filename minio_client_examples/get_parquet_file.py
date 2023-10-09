from minio import Minio

client = Minio(
    "s3.opensky-network.org",
     secure=True
)

# Download file (get filename from list_objects()) (list_files_for_day.py)
client.fget_object(bucket_name="flightsv5", object_name="day=1671408000/part-r-00169-7c325c2d-4d60-41d4-996b-20afd1be8d49.snappy.parquet", file_path="1671408000.snappy.parquet")