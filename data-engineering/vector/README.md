# Vector

- https://hub.docker.com/r/timberio/vector
- https://vector.dev/docs/reference/api/

Access GraphQL API: `http://localhost:8686/playground`.

```graphql
{
  health
  components {
    totalCount
    nodes {
      componentId
      componentType
    }
  }
  sources{
    nodes {
      componentId
      componentType
    }
    totalCount
  }
  transforms {
    totalCount
    nodes {
      componentId
      componentType
    }
  }
  sinks {
    totalCount
    nodes {
      componentId 
      componentType
    }
  }
}
```

## Examples

- [Nginx log => ClickHouse](https://clickhouse.com/docs/en/integrations/vector)

Access `http://localhost:18080/`.

```shell
# clickhouse-client -q "SELECT * FROM devops.log"               
172.18.0.1      2024-04-19 03:04:27     /       200     31      Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36
172.18.0.1      2024-04-19 03:04:27     /favicon.ico    200     31      Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36
```