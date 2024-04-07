from datetime import timedelta
from minio import Minio
from minio.error import S3Error

if __name__ == "__main__":
    client = Minio(endpoint="127.0.0.1:9000",
                   access_key="946Kzk8aC07n0xDCYyMf",
                   secret_key="aOMZkAiUieNQCNgArlfeWLqiYBAubGIZCj8bfNuS",
                   secure=False,
                   cert_check=False,
                   )
    url = client.get_presigned_url(
        "GET",
        "python-test-bucket",
        "file_uploader.txt",
        expires=timedelta(hours=2),
    )
    print(url)
