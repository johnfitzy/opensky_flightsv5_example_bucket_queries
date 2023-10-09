from minio import Minio

client = Minio(
    "s3.opensky-network.org",
     secure=True
)
# Download file (get filename from list_objects()) (list_files_for_day.py)
client.fget_object(bucket_name="flightsv5", object_name="flightsv5_schema.txt", file_path="flightsv5_schema.txt")