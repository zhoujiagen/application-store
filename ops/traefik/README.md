# Traefik
- https://hub.docker.com/_/traefik

```shell
docker compose up -d
docker compose up -d --scale whoami=2
```

Access Dashboard: `http://localhost:18080/`.
- HTTP Routers/Services/Middlewares: http://localhost:18080/dashboard/#/http/routers

Verify:

```shell
curl -H Host:whoami.docker.localhost http://127.0.0.1:180
```