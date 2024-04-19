#-*-coding: UTF-8 -*-

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

import time


# example: https://www.jaegertracing.io/docs/1.56/architecture/#span
# A
# \- B
# \- \- C
# \- \- D
# \- E

def A(tracer):
  with tracer.start_as_current_span("A"):
    print(trace.get_current_span())
    time.sleep(0.11)
    B(tracer)
    E(tracer)
   
def B(tracer):
  with tracer.start_as_current_span("B") as span:
    print(span)
    time.sleep(0.12)
    C(tracer)
    D(tracer)

def C(tracer):
  with tracer.start_as_current_span("C") as span:
    time.sleep(0.13)
    print(span)

def D(tracer):
  with tracer.start_as_current_span("D") as span:
    time.sleep(0.14)
    print(span)

def E(tracer):
  with tracer.start_as_current_span("E") as span:
    time.sleep(0.15)
    print(span)

if __name__=="__main__":
  # Resource can be required for some backends, e.g. Jaeger
  # If resource wouldn't be set - traces wouldn't appears in Jaeger
  resource = Resource(attributes={
      "service.name": "ex_exporter"
  })

  trace.set_tracer_provider(TracerProvider(resource=resource))
  tracer = trace.get_tracer(__name__)

  otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4317", insecure=True)
  span_processor = BatchSpanProcessor(otlp_exporter)
  trace.get_tracer_provider().add_span_processor(span_processor)

  with tracer.start_as_current_span("foo") as span:
    print("Hello world!")
    A(tracer)

