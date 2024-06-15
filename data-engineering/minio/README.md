# MinIO
- https://min.io/docs/minio/container/index.html

Access `http://127.0.0.1:9001/` with `devops/devops+minio`.

Create Access Key:
- Access Key: `946Kzk8aC07n0xDCYyMf`
- Secret Key: `aOMZkAiUieNQCNgArlfeWLqiYBAubGIZCj8bfNuS`
- Policy
```javascript
{
 "Version": "2012-10-17",
 "Statement": [
  {
   "Effect": "Allow",
   "Action": [
    "s3:*"
   ],
   "Resource": [
    "arn:aws:s3:::*"
   ]
  }
 ]
}
```


## Clients

### MC

```shell
mc alias set local http://127.0.0.1:9000 devops devops+minio
mc admin info local
```

### Python

- https://min.io/docs/minio/linux/developers/python/minio-py.html
- examples: https://github.com/minio/minio-py/tree/master/examples

```shell
# Windows WSL
$ python --version
Python 3.11.5
$ python -m virtualenv .venv
$ source .venv/Scripts/activate
$ pip install minio
$ pip freeze > requirements.txt
```

- create bucket and put object

```shell
$ python file_uploader.py 
Created bucket python-test-bucket
file_uploader.py successfully uploaded as object file_uploader.txt to bucket python-test-bucket

# verify
$ mc ls -r local
1.2KiB STANDARD python-test-bucket/file_uploader.txt
```

- get object

```shell
$ python get_object.py
None
b'from minio import Minio\nfrom...
```

- get presigned url

```shell
$ python get_presigned_url.py 
http://127.0.0.1:9000/python-test-bucket/file_uploader.txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=946Kzk8aC07n0xDCYyMf%2F20240407%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240407T090614Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=03bf2a93a53ab4c9804e9869e029a856a5da7f9cfbe9cd1e3076e7889e1ec9b5
```
