from minio import Minio

client = Minio(
    "s3.opensky-network.org",
     secure=True
)

# Get file names for a given day
# example output: day=1671408000/part-r-00169-7c325c2d-4d60-41d4-996b-20afd1be8d49.snappy.parquet
objects = client.list_objects(bucket_name="flightsv5", prefix="day=1671408000/")
for obj in objects:
    print(obj.object_name)