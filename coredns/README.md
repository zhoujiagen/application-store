# CoreDNS

- https://hub.docker.com/r/coredns/coredns
- plugin: https://github.com/coredns/coredns/blob/master/plugin.cfg

## Client

### dig

- https://linux.die.net/man/1/dig

```shell
$ dig -v
DiG 9.16.48-Ubuntu

$ dig @192.168.3.182 -p 1053 -t A -q whoami.example.org
```

## Plugins

### etcd

```shell
# in container etcd
$ etcdctl --endpoints=http://${NODE1}:12379 put /srv/org/devops/services/users '{"host": "192.168.3.182","port": 20020, "priority": 10, "weight": 20}'
$ etcdctl --endpoints=http://${NODE1}:12379 get /srv/org/devops/services/users

$ dig @192.168.3.182 -p 1053 -t SRV +all -q users.services.devops.org
...
;; QUESTION SECTION:
;users.services.devops.org.     IN      SRV

;; ANSWER SECTION:
users.services.devops.org. 300  IN      SRV     10 100 20020 users.services.devops.org.

;; ADDITIONAL SECTION:
users.services.devops.org. 300  IN      A       192.168.3.182
...
```

Verify using dig:

```shell
# in container etcd
$ etcdctl --endpoints=http://${NODE1}:12379 put /srv/org/devops/services/users '{"host": "192.168.3.182","port": 20020, "priority": 10, "weight": 20}'

$ dig @192.168.3.182 -p 1053 -t SRV +all -q users.services.devops.org
...
;; QUESTION SECTION:
;users.services.devops.org.     IN      SRV

;; ANSWER SECTION:
users.services.devops.org. 300  IN      SRV     10 100 20020 users.services.devops.org.

;; ADDITIONAL SECTION:
users.services.devops.org. 300  IN      A       192.168.3.182
...
```

Verify using NodeJS `dns` module:

```javascript
const dns = require('node:dns');
dns.setServers(['192.168.3.182:1053'])
dns.getServers()

// A
dns.resolve4('users.services.devops.org', (err, addresses) => {
  console.log(err)
  console.log(addresses)
});
// [ '192.168.3.182' ]

// SRV
dns.resolveSrv('users.services.devops.org', (err, addresses) => {
  console.log(err)
  console.log(addresses)
});
// [
//   {
//     name: 'users.services.devops.org',
//     port: 20020,
//     priority: 10,
//     weight: 100
//   }
// ]
```
