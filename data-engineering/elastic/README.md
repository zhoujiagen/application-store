# Elastic
- https://www.docker.elastic.co/
- https://github.com/elastic/elasticsearch/tree/7.17/distribution/docker

```shell
├── docker-compose.yml                  # elasticsearch, kibana
├── data                                # elasticsearch data
├── filebeat.yml                        # filebeat settings
├── filebeat-docker-compose.yml         # filebeat
└── kibana.yml                          # kibana settings
```

## Security settings
- https://www.elastic.co/guide/en/elasticsearch/reference/7.17/security-basic-setup.html
- https://www.elastic.co/guide/en/elasticsearch/reference/7.17/configuring-tls-docker.html

```shell
$ pwd
/usr/share/elasticsearch

# CA
$ bin/elasticsearch-certutil ca
Please enter the desired output file [elastic-stack-ca.p12]:
Enter password for elastic-stack-ca.p12 : < esca+apm
# certificate
$ bin/elasticsearch-certutil cert --ca elastic-stack-ca.p12
...
Enter password for CA (elastic-stack-ca.p12) : < esca+apm
Please enter the desired output file [elastic-certificates.p12]:
Enter password for elastic-certificates.p12 : < esc+apm

Certificates written to /usr/share/elasticsearch/elastic-certificates.p12
...

# keystore
$ ./bin/elasticsearch-keystore add xpack.security.transport.ssl.keystore.secure_password
Enter value for xpack.security.transport.ssl.keystore.secure_password: < esc+apm
$ ./bin/elasticsearch-keystore add xpack.security.transport.ssl.truststore.secure_password
Enter value for xpack.security.transport.ssl.truststore.secure_password: < esc+apm
# store in config/elasticsearch.keystore

$ chown elasticsearch *.p12
$ mkdir -p 
$ cp *.p12 data/
```

```shell
$ bin/elasticsearch-setup-passwords interactive
Initiating the setup of passwords for reserved users elastic,apm_system,kibana,kibana_system,logstash_system,beats_system,remote_monitoring_user.
You will be prompted to enter passwords as the process progresses.
Please confirm that you would like to continue [y/N]y


Enter password for [elastic]:
Reenter password for [elastic]:
Enter password for [apm_system]:
Reenter password for [apm_system]:
Enter password for [kibana_system]:
Reenter password for [kibana_system]:
Enter password for [logstash_system]:
Reenter password for [logstash_system]:
Enter password for [beats_system]:
Reenter password for [beats_system]:
Enter password for [remote_monitoring_user]:
Reenter password for [remote_monitoring_user]:
Changed password for user [apm_system]
Changed password for user [kibana_system]
Changed password for user [kibana]
Changed password for user [logstash_system]
Changed password for user [beats_system]
Changed password for user [remote_monitoring_user]
Changed password for user [elastic]


$ bin/elasticsearch-users useradd kibana
Enter new password: < kibana
Retype new password:
$ bin/elasticsearch-users roles -a superuser kibana
# store in config/users, config/user_roles
```