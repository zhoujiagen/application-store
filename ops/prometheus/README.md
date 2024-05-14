# Prometheus based Metrics and Alerts

```shell
├── docker-compose.yml                      # prometheus, prometheus-alertmanager, grafana
├── exporter                                # prometheus exporters
│   ├── docker-compose.yml                  #  currently: cadvisor, mysql, redis, mongodb, elasticsearch
│   ├── mysqld_exporter.config.my-conf
│   └── node_exporter-1.6.1.linux-amd64     #  node exporter
│       ├── README.txt
│       └── start_node_exporter.sh
├── grafana_data                            # grafana data
├── prometheus-alertmanager-data            # prometheus-alertmanager data
├── prometheus-alertmanager.yml             # prometheus-alertmanager receiver settings, etc
├── prometheus-data                         # prometheus data
├── prometheus-rules.yml                    # prometheus settings on rules, currently only altering rules
├── prometheus-web.yml                      # prometheus basic auth settings
└── prometheus.yml                          # prometheus settings on scrape, rule files, altermanager
```