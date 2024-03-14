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

5. Cleanup

```shell
$ kubectl -n devops delete -f samples/bookinfo/networking/bookinfo-gateway.yaml
$ kubectl -n devops delete -f samples/bookinfo/platform/kube/bookinfo.yaml
service "details" deleted
serviceaccount "bookinfo-details" deleted
deployment.apps "details-v1" deleted
service "ratings" deleted
serviceaccount "bookinfo-ratings" deleted
deployment.apps "ratings-v1" deleted
service "reviews" deleted
serviceaccount "bookinfo-reviews" deleted
deployment.apps "reviews-v1" deleted
deployment.apps "reviews-v2" deleted
deployment.apps "reviews-v3" deleted
service "productpage" deleted
serviceaccount "bookinfo-productpage" deleted
deployment.apps "productpage-v1" deleted


$ kubectl delete -f samples/addons/
serviceaccount "grafana" deleted
configmap "grafana" deleted
service "grafana" deleted
deployment.apps "grafana" deleted
configmap "istio-grafana-dashboards" deleted
configmap "istio-services-grafana-dashboards" deleted
deployment.apps "jaeger" deleted
service "tracing" deleted
service "zipkin" deleted
service "jaeger-collector" deleted
serviceaccount "kiali" deleted
configmap "kiali" deleted
clusterrole.rbac.authorization.k8s.io "kiali-viewer" deleted
clusterrole.rbac.authorization.k8s.io "kiali" deleted
clusterrolebinding.rbac.authorization.k8s.io "kiali" deleted
role.rbac.authorization.k8s.io "kiali-controlplane" deleted
rolebinding.rbac.authorization.k8s.io "kiali-controlplane" deleted
service "kiali" deleted
deployment.apps "kiali" deleted
serviceaccount "loki" deleted
configmap "loki" deleted
configmap "loki-runtime" deleted
service "loki-memberlist" deleted
service "loki-headless" deleted
service "loki" deleted
statefulset.apps "loki" deleted
serviceaccount "prometheus" deleted
configmap "prometheus" deleted
clusterrole.rbac.authorization.k8s.io "prometheus" deleted
clusterrolebinding.rbac.authorization.k8s.io "prometheus" deleted
service "prometheus" deleted
deployment.apps "prometheus" deleted

$ bin/istioctl.exe uninstall -y --purge
All Istio resources will be pruned from the cluster

  Removed IstioOperator:istio-system:installed-state.
  Removed Deployment:istio-system:istio-egressgateway.
  Removed Deployment:istio-system:istio-ingressgateway.
  Removed Deployment:istio-system:istiod.
  Removed Service:istio-system:istio-egressgateway.
  Removed Service:istio-system:istio-ingressgateway.
  Removed Service:istio-system:istiod.
  Removed ConfigMap:istio-system:istio.
  Removed ConfigMap:istio-system:istio-sidecar-injector.
  Removed Pod:istio-system:istio-egressgateway-687cb674fc-4djmj.
  Removed Pod:istio-system:istio-ingressgateway-85c5875ff7-dplpw.
  Removed Pod:istio-system:istiod-7fb4d64fb6-5tw6p.
  Removed ServiceAccount:istio-system:istio-egressgateway-service-account.
  Removed ServiceAccount:istio-system:istio-ingressgateway-service-account.
  Removed ServiceAccount:istio-system:istio-reader-service-account.
  Removed ServiceAccount:istio-system:istiod.
  Removed RoleBinding:istio-system:istio-egressgateway-sds.
  Removed RoleBinding:istio-system:istio-ingressgateway-sds.
  Removed RoleBinding:istio-system:istiod.
  Removed Role:istio-system:istio-egressgateway-sds.
  Removed Role:istio-system:istio-ingressgateway-sds.
  Removed Role:istio-system:istiod.
  Removed PodDisruptionBudget:istio-system:istio-egressgateway.
  Removed PodDisruptionBudget:istio-system:istio-ingressgateway.
  Removed PodDisruptionBudget:istio-system:istiod.
  Removed MutatingWebhookConfiguration::istio-revision-tag-default.
  Removed MutatingWebhookConfiguration::istio-sidecar-injector.
  Removed ValidatingWebhookConfiguration::istio-validator-istio-system.
  Removed ValidatingWebhookConfiguration::istiod-default-validator.
  Removed ClusterRole::istio-reader-clusterrole-istio-system.
  Removed ClusterRole::istiod-clusterrole-istio-system.
  Removed ClusterRole::istiod-gateway-controller-istio-system.
  Removed ClusterRoleBinding::istio-reader-clusterrole-istio-system.
  Removed ClusterRoleBinding::istiod-clusterrole-istio-system.
  Removed ClusterRoleBinding::istiod-gateway-controller-istio-system.
  Removed CustomResourceDefinition::authorizationpolicies.security.istio.io.
  Removed CustomResourceDefinition::destinationrules.networking.istio.io.
  Removed CustomResourceDefinition::envoyfilters.networking.istio.io.
  Removed CustomResourceDefinition::gateways.networking.istio.io.
  Removed CustomResourceDefinition::istiooperators.install.istio.io.
  Removed CustomResourceDefinition::peerauthentications.security.istio.io.
  Removed CustomResourceDefinition::proxyconfigs.networking.istio.io.
  Removed CustomResourceDefinition::requestauthentications.security.istio.io.
  Removed CustomResourceDefinition::serviceentries.networking.istio.io.
  Removed CustomResourceDefinition::sidecars.networking.istio.io.
  Removed CustomResourceDefinition::telemetries.telemetry.istio.io.
  Removed CustomResourceDefinition::virtualservices.networking.istio.io.
  Removed CustomResourceDefinition::wasmplugins.extensions.istio.io.
  Removed CustomResourceDefinition::workloadentries.networking.istio.io.
  Removed CustomResourceDefinition::workloadgroups.networking.istio.io.
✔ Uninstall complete                       

$ kubectl delete namespace istio-system
namespace "istio-system" deleted

$ kubectl describe ns devops
Name:         devops
Labels:       istio-injection=enabled
              kubernetes.io/metadata.name=devops
Annotations:  <none>
Status:       Active

No resource quota.

No LimitRange resource.

$ kubectl label namespace devops istio-injection-
namespace/devops unlabeled

$ kubectl delete ns devops
namespace "devops" deleted
```