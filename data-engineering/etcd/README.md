# etcd

- https://etcd.io/docs/v3.5/op-guide/container/
- https://hub.docker.com/r/bitnami/etcd

## Clients

- https://etcd.io/docs/v3.5/integrations/

### etcdctl

```shell
$ etcdctl --endpoints=http://${NODE1}:12379 member list
11503d5365d7ce8e, started, etcd, http://192.168.3.182:12380, http://192.168.3.182:12379, false

$ etcdctl --endpoints=http://${NODE1}:12379 put greeting "hello, etcd"
OK

$ etcdctl --endpoints=http://${NODE1}:12379 get greeting
greeting
hello, etcd
```

Cluster:

```shell
# etcd-node-1
$ etcdctl --endpoints=http://${THIS_NAME}:12379 member list
c57b251520efec6, started, etcd-node-2, http://192.168.3.182:12381, http://192.168.3.182:12378, false
55bfe9700873088c, started, etcd-node-1, http://192.168.3.182:12380, http://192.168.3.182:12379, false
b6f383d984945c94, started, etcd-node-3, http://192.168.3.182:12382, http://192.168.3.182:12377, false

$ etcdctl --endpoints=http://${THIS_NAME}:12379 put greeting "hello, etcd"
OK
$ etcdctl --endpoints=http://${THIS_NAME}:12379 get greeting
greeting
hello, etcd

# etcd-node-2
$ etcdctl --endpoints=http://${THIS_NAME}:12378 member list
c57b251520efec6, started, etcd-node-2, http://192.168.3.182:12381, http://192.168.3.182:12378, false
55bfe9700873088c, started, etcd-node-1, http://192.168.3.182:12380, http://192.168.3.182:12379, false
b6f383d984945c94, started, etcd-node-3, http://192.168.3.182:12382, http://192.168.3.182:12377, false
$ etcdctl --endpoints=http://${THIS_NAME}:12378 get greeting
greeting
hello, etcd

# etcd-node-3
$ etcdctl --endpoints=http://${THIS_NAME}:12377 get greeting
greeting
hello, etcd
```

Enable authentication:

```shell
# etcd-node-1
$ etcdctl --endpoints=http://${THIS_NAME}:12379 role add root
Role root created
$ etcdctl --endpoints=http://${THIS_NAME}:12379 user add root
Password of root:
Type password of root again for confirmation:
User root created
$ etcdctl --endpoints=http://${THIS_NAME}:12379 user grant-role root root
Role root is granted to user root
$ etcdctl --endpoints=http://${THIS_NAME}:12379 auth enable
Authentication Enabled

$ etcdctl --endpoints=http://${THIS_NAME}:12379 get greeting
Error: etcdserver: user name is empty
$ etcdctl --endpoints=http://${THIS_NAME}:12379 get greeting --user=root
Password:
greeting
hello, etcd
$ etcdctl --endpoints=http://${THIS_NAME}:12379 get greeting --user=root:devops+etcd
greeting
hello, etcd
```

### Python

- https://github.com/kragniz/python-etcd3

```shell
# Windows WSL
$ python --version
Python 3.8.10
$ python -m virtualenv .venv

$ source .venv/bin/activate
$ pip install etcd3

# downgrade grpcio and protobuf
# https://github.com/grpc/grpc/issues/29643
# https://github.com/kragniz/python-etcd3/blob/master/requirements/base.txt
# https://pypi.org/project/grpcio/
pip uninstall grpcio
pip install grpcio==1.38.0
pip uninstall protobuf
pip install protobuf==3.17.0

$ pip freeze > requirements.txt
```

```shell
$ python ex_etcd.py
(b'dooot', <etcd3.client.KVMetadata object at 0x7f3851918b80>)
```