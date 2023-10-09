from minio import Minio

client = Minio(
    "s3.opensky-network.org",
     secure=True
)
# Get dates for which FlightsV5 files are present
objects = client.list_objects(bucket_name="flightsv5", "day=*")
for obj in objects:
    print(obj.object_name)