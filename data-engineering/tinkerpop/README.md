# TinkerPop

- https://hub.docker.com/u/tinkerpop
- [gremlin-console](https://tinkerpop.apache.org/docs/current/reference/#gremlin-console)
- [gremlin-server](https://tinkerpop.apache.org/docs/current/reference/#gremlin-server)


```shell
# copy configurations
# Windows
docker container cp gremlin-server:/opt/gremlin-server/conf .\server-conf\
docker container cp gremlin-console:/opt/gremlin-console/conf .\console-conf\
```

## Clients

### HTTP

- `gremlin-server-rest-modern.yaml`

```shell
curl --request GET \
  --url 'http://127.0.0.1:8182/?gremlin=100-1'

curl --request POST \
  --url http://127.0.0.1:8182/ \
  --header 'Content-Type: application/json' \
  --data '{
  "gremlin": "100-x",
  "bindings": {
    "x": 1
  },
  "language": "gremlin-groovy"
}'
```

### gremlin-console

```shell
# gremlin-console
$ bin/gremlin.sh
gremlin> :remote connect tinkerpop.server conf/remote.yaml
==>Configured gremlin-server/172.18.0.2:8182
gremlin> :remote console
==>All scripts will now be sent to Gremlin Server - [gremlin-server/172.18.0.2:8182] - type ':remote console' to return to local mode
gremlin> g
==>graphtraversalsource[tinkergraph[vertices:0 edges:0], standard]
```

Load Groovy scripts:

```shell
$ bin/gremlin.sh -i scripts/gia.groovy
gremlin> g
==>graphtraversalsource[tinkergraph[vertices:8 edges:12], standard]
```

### Alchemy.js

- https://graphalchemist.github.io/Alchemy

[Alchemy.html](./clients/Alchemy/Alchemy.html)

