# Harbor

- https://goharbor.io/

## About Certificates

```shell
# Windows WSL
# CA certificate
openssl genrsa -out ca.key 4096
openssl req -x509 -new -nodes -sha512 -days 3650 \
 -subj "/C=CN/ST=Shanghai/L=Shanghai/O=devops/OU=Personal/CN=172.22.152.92" \
 -key ca.key \
 -out ca.crt

# Server certificate
openssl genrsa -out 172.22.152.92.key 4096

openssl req -sha512 -new \
    -subj "/C=CN/ST=Shanghai/L=Shanghai/O=devops/OU=Personal/CN=172.22.152.92" \
    -key 172.22.152.92.key \
    -out 172.22.152.92.csr

# DEPLOY_ENV
cat > v3.ext <<-EOF
authorityKeyIdentifier=keyid,issuer
basicConstraints=CA:FALSE
keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
extendedKeyUsage = serverAuth
subjectAltName = @alt_names

[alt_names]
IP.1=172.22.152.92
IP.2=192.168.3.135
IP.3=127.0.0.1
EOF

openssl x509 -req -sha512 -days 3650 \
    -extfile v3.ext \
    -CA ca.crt -CAkey ca.key -CAcreateserial \
    -in 172.22.152.92.csr \
    -out 172.22.152.92.crt

# for Docker
# WARN: Cannot find effectice setting on daemon.json for Windwos Docker Desktop.
openssl x509 -inform PEM -in 172.22.152.92.crt -out 172.22.152.92.cert
```

Install `ca.crt` and `172.22.152.92.cert`, and add `ca.crt` to trusted root CA.

## Setup

```shell
# Windows WSL
$ ./prepare
prepare base dir is set to /mnt/d/workspace/application-store/harbor/harbor
Clearing the configuration file: /config/core/app.conf
Clearing the configuration file: /config/core/env
Clearing the configuration file: /config/db/env
Clearing the configuration file: /config/jobservice/config.yml
Clearing the configuration file: /config/jobservice/env
Clearing the configuration file: /config/log/logrotate.conf
Clearing the configuration file: /config/log/rsyslog_docker.conf
Clearing the configuration file: /config/nginx/nginx.conf
Clearing the configuration file: /config/portal/nginx.conf
Clearing the configuration file: /config/registry/config.yml
Clearing the configuration file: /config/registry/passwd
Clearing the configuration file: /config/registry/root.crt
Clearing the configuration file: /config/registryctl/config.yml
Clearing the configuration file: /config/registryctl/env
Generated configuration file: /config/portal/nginx.conf
Generated configuration file: /config/log/logrotate.conf
Generated configuration file: /config/log/rsyslog_docker.conf
Generated configuration file: /config/nginx/nginx.conf
Generated configuration file: /config/core/env
Generated configuration file: /config/core/app.conf
Generated configuration file: /config/registry/config.yml
Generated configuration file: /config/registryctl/env
Generated configuration file: /config/registryctl/config.yml
Generated configuration file: /config/db/env
Generated configuration file: /config/jobservice/env
Generated configuration file: /config/jobservice/config.yml
loaded secret from file: /data/secret/keys/secretkey
Generated configuration file: /compose_location/docker-compose.yml
Clean up the input dir

$ ./install.sh

[Step 0]: checking if docker is installed ...

Note: docker version: 24.0.5

[Step 1]: checking docker-compose is installed ...

Note: Docker Compose version v2.20.2-desktop.1

[Step 2]: loading Harbor images ...
Loaded image: goharbor/harbor-portal:v2.10.1
Loaded image: goharbor/harbor-db:v2.10.1
Loaded image: goharbor/redis-photon:v2.10.1
Loaded image: goharbor/nginx-photon:v2.10.1
Loaded image: goharbor/prepare:v2.10.1
Loaded image: goharbor/harbor-core:v2.10.1
Loaded image: goharbor/harbor-log:v2.10.1
Loaded image: goharbor/harbor-jobservice:v2.10.1
Loaded image: goharbor/harbor-registryctl:v2.10.1
Loaded image: goharbor/harbor-exporter:v2.10.1
Loaded image: goharbor/registry-photon:v2.10.1
Loaded image: goharbor/trivy-adapter-photon:v2.10.1


[Step 3]: preparing environment ...

[Step 4]: preparing harbor configs ...
prepare base dir is set to /mnt/d/workspace/application-store/harbor/harbor
Clearing the configuration file: /config/core/app.conf
Clearing the configuration file: /config/core/env
Clearing the configuration file: /config/db/env
Clearing the configuration file: /config/jobservice/config.yml
Clearing the configuration file: /config/jobservice/env
Clearing the configuration file: /config/log/logrotate.conf
Clearing the configuration file: /config/log/rsyslog_docker.conf
Clearing the configuration file: /config/nginx/nginx.conf
Clearing the configuration file: /config/portal/nginx.conf
Clearing the configuration file: /config/registry/config.yml
Clearing the configuration file: /config/registry/passwd
Clearing the configuration file: /config/registry/root.crt
Clearing the configuration file: /config/registryctl/config.yml
Clearing the configuration file: /config/registryctl/env
Generated configuration file: /config/portal/nginx.conf
Generated configuration file: /config/log/logrotate.conf
Generated configuration file: /config/log/rsyslog_docker.conf
Generated configuration file: /config/nginx/nginx.conf
Generated configuration file: /config/core/env
Generated configuration file: /config/core/app.conf
Generated configuration file: /config/registry/config.yml
Generated configuration file: /config/registryctl/env
Generated configuration file: /config/registryctl/config.yml
Generated configuration file: /config/db/env
Generated configuration file: /config/jobservice/env
Generated configuration file: /config/jobservice/config.yml
loaded secret from file: /data/secret/keys/secretkey
Generated configuration file: /compose_location/docker-compose.yml
Clean up the input dir


Note: stopping existing Harbor instance ...
[+] Running 10/10
 ✔ Container harbor-jobservice  Removed                                               1.1s
 ✔ Container registryctl        Removed                                               0.9s
 ✔ Container nginx              Removed                                               1.0s
 ✔ Container harbor-portal      Removed                                               0.4s
 ✔ Container harbor-core        Removed                                               4.6s
 ✔ Container harbor-db          Removed                                               0.9s
 ✔ Container registry           Removed                                               0.7s
 ✔ Container redis              Removed                                               0.8s
 ✔ Container harbor-log         Removed                                               10.4s
 ✔ Network harbor_harbor        Removed                                               0.2s


[Step 5]: starting Harbor ...
[+] Running 10/10
 ✔ Network harbor_harbor        Created                                               0.0s
 ✔ Container harbor-log         Started                                               0.6s
 ✔ Container harbor-db          Started                                               1.5s
 ✔ Container harbor-portal      Started                                               1.0s
 ✔ Container registry           Started                                               1.4s
 ✔ Container redis              Started                                               1.2s
 ✔ Container registryctl        Started                                               1.4s
 ✔ Container harbor-core        Started                                               1.7s
 ✔ Container nginx              Started                                               2.1s
 ✔ Container harbor-jobservice  Started                                               2.2s
✔ ----Harbor has been installed and started successfully.----
```

Access `https://172.22.152.92/` with `admin/Harbor12345`.