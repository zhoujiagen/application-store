#-*-coding: UTF-8 -*-

import ldap
import pprint

# data: plainjoe.ldif, example from 'LDAP System Administration'
if __name__=="__main__":
  l = ldap.initialize("ldap://localhost:389")
  l.simple_bind_s("cn=devops,dc=devops,dc=org","devops+openldap")
  res = l.search_s("dc=devops,dc=org", ldap.SCOPE_SUBTREE, "objectclass=*")
  pprint.pprint(res)