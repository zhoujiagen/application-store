# OpenLDAP

- https://hub.docker.com/r/bitnami/openldap/
- https://www.openldap.org

```shell
$ bin/ldapsearch -x -b '' -s base '(objectclass=*)' namingContexts
$ bin/ldapsearch -x -b 'dc=devops,dc=org' '(objectclass=*)'

# Schemas
I have no name!@a298631e23bd:/opt/bitnami/openldap/etc$ ls schema/
README             corba.schema  cosine.schema  duaconf.schema      inetorgperson.schema  misc.schema       namedobject.schema  openldap.schema
collective.ldif    core.ldif     dsee.ldif      dyngroup.ldif       java.ldif             msuser.ldif       nis.ldif            pmi.ldif
collective.schema  core.schema   dsee.schema    dyngroup.schema     java.schema           msuser.schema     nis.schema          pmi.schema
corba.ldif         cosine.ldif   duaconf.ldif   inetorgperson.ldif  misc.ldif             namedobject.ldif  openldap.ldif
```

## Clients

### UI

- [Apache Directory Studio™](https://directory.apache.org/studio/)

Simple authentication:

```
# Bind DN or user
cn=devopsadmin,cn=config
# Bind password
devopsadmin+openldap

cn=devops,dc=devops,dc=org
devops+openldap
```

### Python

- https://github.com/python-ldap/python-ldap
- [flask-simpleldap](https://github.com/alexferl/flask-simpleldap)

```shell
# Windows WSL
$ sudo apt-get install build-essential python3-dev python3-virtualenv libc6-dbg    libldap2-dev libsasl2-dev slapd ldap-utils tox     lcov valgrind
$ pip install python-ldap

$ python3 ex_openldap.py
[('dc=devops,dc=org',
  {'dc': [b'devops'],
   'o': [b'example'],
   'objectClass': [b'dcObject', b'organization']}),
 ('ou=users,dc=devops,dc=org',
  {'objectClass': [b'organizationalUnit'], 'ou': [b'users']}),
...
]
```


