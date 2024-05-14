# Jaeger

Jaeger UI: `http://localhost:16686/`.

## Clients
- https://www.jaegertracing.io/docs/1.56/client-libraries

### Python
- https://www.jaegertracing.io/docs/1.56/client-libraries/#python
- https://opentelemetry-python.readthedocs.io/en/latest/exporter/otlp/otlp.html

```shell
$ python -m virtualenv .venv
$ source .venv/Scripts/activate

$ pip install opentelemetry-api
$ pip install opentelemetry-sdk
$ pip install opentelemetry-exporter-otlp

$ pip freeze > requirements.txt
```