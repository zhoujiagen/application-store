#-*-coding: UTF-8 -*-

import etcd3

# ref: https://github.com/kragniz/python-etcd3
if __name__=="__main__":
  etcd = etcd3.client(
    host="192.168.3.182", port=12379,
    user="root", password="devops+etcd") # DEPLOY_ENV
  
  etcd.put('/key', 'dooot')
  print(etcd.get('/key'))

  # TODO: lock, transaction, watches
