# Neo4j

- https://hub.docker.com/_/neo4j/

Access http://localhost:7474/

Example property graph database: [neo4j-graph-examples/movies](https://github.com/neo4j-graph-examples/movies/blob/main/scripts/movies.cypher).

Cypher queries:

```cypher
MATCH (n)
RETURN n
```

## Clients

### JavaScript
- https://neo4j.com/docs/javascript-manual/current/

```shell
npm init
npm i neo4j-driver
npm i -D nodemon
npm run dev
```
