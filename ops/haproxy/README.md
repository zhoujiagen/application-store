# HAProxy
- https://hub.docker.com/_/haproxy/

Test the configuration file:
```shell
haproxy -f /usr/local/etc/haproxy/haproxy.cfg -c
```

HTTP backend: [run.sh](../../testing/flask/run.sh)
- http://localhost:8888/

TCP backend: [run.sh](../../testing/tcp-echo/run.sh)
```shell
$ telnet 192.168.3.181 8889

192.168.3.181:8001 > aaa
what
192.168.3.181:8001 > what
exit

Connection to host lost.
```

stats UI: http://localhost:20936/haproxy?stats
- auth: `admin:password`

stats socket:
```shell
➜  ~ echo "help" | nc 192.168.3.181 9999
The following commands are valid at this level:
  abort ssl ca-file <cafile>              : abort a transaction for a CA file
  ...
➜  ~ echo "show sess" | nc 192.168.3.181 9999
0x7f6bfc03f6e0: proto=tcpv4 src=172.18.0.1:52342 fe=GLOBAL be=<NONE> srv=<none> ts=00 epoch=0 age=0s calls=1 rate=0 cpu=0 lat=0 rq[f=848101h,i=0,an=00h,ax=] rp[f=80008000h,i=0,an=00h,ax=] scf=[8,0h,fd=71,rex=30s,wex=] scb=[8,1h,fd=-1,rex=,wex=] exp=29s rc=0 c_exp=
```