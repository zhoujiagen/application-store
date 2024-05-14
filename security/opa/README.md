# opa: Open Policy Agent

- https://www.openpolicyagent.org/
- VSCode extension: https://marketplace.visualstudio.com/items?itemName=tsandall.opa

```shell
$ docker compose up -d

$ docker exec -it opa-server opa version
Version: 0.62.1
Build Commit: a4d77da064b825fc6c62f1ce53b5da27af476a7b
Build Timestamp: 2024-03-06T10:26:57Z
Build Hostname: 0769577eafc2
Go Version: go1.22.1
Platform: linux/amd64
WebAssembly: available
```

## example.rego

- Web


Query:

```rego
input.servers[i].ports[_] = "p2"; input.servers[i].id = id
```

Input Data(JSON): see `examples/input.json`

Result:

```json
{
  "result": [
    {
      "i": 0,
      "id": "app"
    },
    {
      "i": 3,
      "id": "ci"
    }
  ]
}
```

```shell
$ curl localhost:8181/v1/data/example/violation -d @examples/v1-data-input.json -H 'Content-Type: applin/json'
{"decision_id":"ea1b1a38-ba8f-478c-a943-54f4c89a9d00","result":["busybox","ci"]}

$ curl localhost:8181/v1/data/example/allow -d @examples/v1-data-input.json -H 'Content-Type: applin/json'
{"decision_id":"8c1303fa-eae6-4665-9b89-01f30d76804f","result":false}
```

- repl

```shell
$ docker exec -it opa-server opa run /opa-examples/example.rego repl.input:/opa-examples/input.json
OPA 0.62.1 (commit a4d77da064b825fc6c62f1ce53b5da27af476a7b, built at 2024-03-06T10:26:57Z)

Run 'help' to see a list of commands and check for updates.

> package example
> some x; violation[x]
+-----------+--------------+
|     x     | violation[x] |
+-----------+--------------+
| "busybox" | "busybox"    |
| "ci"      | "ci"         |
+-----------+--------------+
```

## system.rego

Use `opa.ipynb` to create Policy `example1`.

By default `data.system.main` is used to serve policy queries without a path. 
When you execute queries without providing a path, you do not have to wrap the `input`. 

```shell
$ curl localhost:8181 -H 'Content-Type: application/json' -d '{ "user": [ "alice" ]}'
"hello, [\"alice\"]"

$ curl localhost:8181/v1/data/system/main -H 'Content-Type: application/json' -d '{ "input": { "user": [ "alice" ] } }'
{"decision_id":"90066aea-83c3-45b4-814b-830792953ded","result":"hello, [\"alice\"]"}
```

## Use Cases

- `opa.ipynb`
