from datetime import timedelta
from minio import Minio
from minio.error import S3Error

if __name__ == "__main__":
    bucket_name = "python-test-bucket"
    object_name = "file_uploader.txt"

    client = Minio(endpoint="127.0.0.1:9000",
                   access_key="946Kzk8aC07n0xDCYyMf",
                   secret_key="aOMZkAiUieNQCNgArlfeWLqiYBAubGIZCj8bfNuS",
                   secure=False,
                   cert_check=False,
                   )
    tags = client.get_object_tags(bucket_name, object_name)
    print(tags)

    try:
        response = client.get_object(bucket_name, object_name)
        # Read data from response.
        print(str(response.data))
        # with open("./minio/clients/python/"+object_name, "wb") as f:
        #     f.write(response.data)
    finally:
        response.close()
        response.release_conn()
