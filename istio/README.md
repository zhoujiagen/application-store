# Istio

1. Install

```shell
# Windows
$ curl -L https://istio.io/downloadIstio | ISTIO_VERSION=1.20.3 sh -
$ cd istio-1.20.3

$ bin/istioctl.exe version
no ready Istio pods in "istio-system"
1.20.3

$ bin/istioctl.exe profile list
Istio configuration profiles:
    ambient
    default
    demo
    empty
    external
    minimal
    openshift
    preview
    remote
```

```shell
$ bin/istioctl.exe install --set profile=demo -y
✔ Istio core installed
✔ Istiod installed
✔ Ingress gateways installed
✔ Egress gateways installed
✔ Installation complete
Made this installation the default for injection and validation.

$ kubectl create namespace devops
$ kubectl label namespace devops istio-injection=enabled
namespace/devops labeled
```

2. Deploy sample application

```shell
$ kubectl -n devops apply -f samples/bookinfo/platform/kube/bookinfo.yaml
service/details created
serviceaccount/bookinfo-details created
deployment.apps/details-v1 created
service/ratings created
serviceaccount/bookinfo-ratings created
deployment.apps/ratings-v1 created
service/reviews created
serviceaccount/bookinfo-reviews created
deployment.apps/reviews-v1 created
deployment.apps/reviews-v2 created
deployment.apps/reviews-v3 created
service/productpage created

$ kubectl -n devops get deployments
NAME             READY   UP-TO-DATE   AVAILABLE   AGE
details-v1       1/1     1            1           8m31s
productpage-v1   1/1     1            1           8m31s
ratings-v1       1/1     1            1           8m31s
reviews-v1       1/1     1            1           8m31s
reviews-v2       1/1     1            1           8m31s
reviews-v3       1/1     1            1           8m31s

$ kubectl -n devops exec "$(kubectl -n devops get pod -l app=ratings -o jsonpath='{.items[0].metadata.name}')" -c ratings -- curl -sS productpage:9080/productpage | grep -o "<title>.*</title>"
I0313 19:35:30.633476   12032 log.go:194] (0xc00023a0b0) (0xc0002a4320) Create stream
I0313 19:35:30.637895   12032 log.go:194] (0xc00023a0b0) (0xc0002a4320) Stream added, broadcasting: 1
I0313 19:35:30.641246   12032 log.go:194] (0xc00023a0b0) Reply frame received for 1
I0313 19:35:30.641246   12032 log.go:194] (0xc00023a0b0) (0xc000228000) Create stream
I0313 19:35:30.641246   12032 log.go:194] (0xc00023a0b0) (0xc000228000) Stream added, broadcasting: 3
I0313 19:35:30.642349   12032 log.go:194] (0xc00023a0b0) Reply frame received for 3
I0313 19:35:30.642349   12032 log.go:194] (0xc00023a0b0) (0xc000228140) Create stream
I0313 19:35:30.642349   12032 log.go:194] (0xc00023a0b0) (0xc000228140) Stream added, broadcasting: 5
I0313 19:35:30.643587   12032 log.go:194] (0xc00023a0b0) Reply frame received for 5
I0313 19:35:31.062813   12032 log.go:194] (0xc00023a0b0) Data frame received for 3
I0313 19:35:31.062813   12032 log.go:194] (0xc000228000) (3) Data frame handling
I0313 19:35:31.062813   12032 log.go:194] (0xc000228000) (3) Data frame sent
I0313 19:35:31.065861   12032 log.go:194] (0xc00023a0b0) (0xc000228140) Stream removed, broadcasting: 5
I0313 19:35:31.065861   12032 log.go:194] (0xc00023a0b0) Data frame received for 1
I0313 19:35:31.065861   12032 log.go:194] (0xc00023a0b0) (0xc000228000) Stream removed, broadcasting: 3
I0313 19:35:31.065861   12032 log.go:194] (0xc0002a4320) (1) Data frame handling
I0313 19:35:31.065861   12032 log.go:194] (0xc0002a4320) (1) Data frame sent
I0313 19:35:31.065861   12032 log.go:194] (0xc00023a0b0) (0xc0002a4320) Stream removed, broadcasting: 1
I0313 19:35:31.066459   12032 log.go:194] (0xc00023a0b0) Go away received
I0313 19:35:31.066459   12032 log.go:194] (0xc00023a0b0) (0xc000228000) Stream removed, broadcasting: 3
I0313 19:35:31.066459   12032 log.go:194] (0xc00023a0b0) (0xc000228140) Stream removed, broadcasting: 5
I0313 19:35:31.066459   12032 log.go:194] (0xc00023a0b0) (0xc0002a4320) Stream removed, broadcasting: 1
<title>Simple Bookstore App</title>
```

3. Create Ingress Gateway

```shell
$ kubectl -n devops apply -f samples/bookinfo/networking/bookinfo-gateway.yaml
gateway.networking.istio.io/bookinfo-gateway created
virtualservice.networking.istio.io/bookinfo created

$ bin/istioctl.exe -n devops analyze

✔ No validation issues found when analyzing namespace: devops.
```

```shell
$ kubectl -n istio-system get svc istio-ingressgateway 
NAME                   TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)                                                                      AGE
istio-ingressgateway   LoadBalancer   10.102.2.114   localhost     15021:32491/TCP,80:30039/TCP,443:30974/TCP,31400:30320/TCP,15443:32642/TCP   21m
```

Assess: `http://localhost/productpage`


4. Install addons

```shell
$ kubectl apply -f samples/addons
$ kubectl -n istio-system get pods
NAME                                    READY   STATUS    RESTARTS   AGE
grafana-5f9b8c6c5d-6wtqj                1/1     Running   0          4m59s
istio-egressgateway-687cb674fc-4djmj    1/1     Running   0          33m
istio-ingressgateway-85c5875ff7-dplpw   1/1     Running   0          33m
istiod-7fb4d64fb6-5tw6p                 1/1     Running   0          33m
jaeger-db6bdfcb4-j8757                  1/1     Running   0          4m59s
kiali-cc67f8648-kjfg8                   1/1     Running   0          4m59s
prometheus-5d5d6d6fc-vv8tm              2/2     Running   0          4m58s
$ kubectl get pods
NAME     READY   STATUS    RESTARTS   AGE
loki-0   1/1     Running   0          5m49s
```

View Kiali Dashboard:

```shell
$ bin/istioctl.exe dashboard kiali
http://localhost:20001/kiali

# generate payload
for i in $(seq 1 100); do curl -s -o /dev/null "http://localhost/productpage"; done
```
