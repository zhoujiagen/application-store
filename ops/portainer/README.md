# Portainer

- https://docs.portainer.io/start/install-ce/server/docker/linux
- https://github.com/portainer/portainer

```shell
docker volume create portainer_data
```

Access `https://localhost:19443`.

```txt
admin+devops+portainer
```

Add Environment:
- Docker Standalone
- Kubernetes: Edge Agent Standard

```shell
# Kubernetes: Edge Agent Standard workaround in community edition
# https://github.com/portainer/portainer/issues/6251

# source token
# curl https://downloads.portainer.io/ee2-20/portainer-edge-agent-setup.sh | bash -s -- "6a961d44-e764-432b-968a-2dce6bca91a0" "aHR0cHM6Ly8xOTIuMTY4LjMuMTg5OjE5NDQzfDE5Mi4xNjguMy4xODk6ODAwMHxTSEYrZTI1ekx2QzIwYm94WVVzREhtTEhXbHlRdDU3TENIbHM2aFNlSmpnPXwxMA" "1" "" ""
# base64 decode
# host IP: 192.168.3.189
https://192.168.3.189:19443|192.168.3.189:8000|SHF+e25zLvC20boxYUsDHmLHWlyQt57LCHls6hSeJjg=|10

# change 192.168.3.189:8000 to 192.168.3.189:18000
# base64 encode
aHR0cHM6Ly8xOTIuMTY4LjMuMTg5OjE5NDQzfDE5Mi4xNjguMy4xODk6MTgwMDB8U0hGK2UyNXpMdkMyMGJveFlVc0RIbUxIV2x5UXQ1N0xDSGxzNmhTZUpqZz18MTA=
# remove trailing =
curl https://downloads.portainer.io/ee2-20/portainer-edge-agent-setup.sh | bash -s -- "6a961d44-e764-432b-968a-2dce6bca91a0" "aHR0cHM6Ly8xOTIuMTY4LjMuMTg5OjE5NDQzfDE5Mi4xNjguMy4xODk6MTgwMDB8U0hGK2UyNXpMdkMyMGJveFlVc0RIbUxIV2x5UXQ1N0xDSGxzNmhTZUpqZz18MTA" "1" "" ""

# log of portainer-agent
# client: Connecting to ws://192.168.3.189:18000
```

cleanup:

```shell
$ kubectl delete -f portainer-agent-edge-k8s.yaml
$ docker compose down
```