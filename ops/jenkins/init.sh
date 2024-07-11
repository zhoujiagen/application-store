/usr/bin/dockerd -H unix:// &

/usr/bin/tini -- /usr/local/bin/jenkins.sh