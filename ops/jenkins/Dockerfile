# https://github.com/jenkinsci/docker/blob/master/debian/bookworm/hotspot/Dockerfile
FROM jenkins/jenkins:lts-jdk17
USER root

# maven
RUN apt-get update && apt-get install -y maven

# skaffold
RUN curl -Lo skaffold https://storage.googleapis.com/skaffold/releases/latest/skaffold-linux-amd64 && \
  install skaffold /usr/local/bin/

# docker
# https://docs.docker.com/engine/install/debian/
# Add Docker's official GPG key:
# RUN apt-get update
RUN apt-get install -y ca-certificates curl && \
  install -m 0755 -d /etc/apt/keyrings
RUN curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc && \
  chmod a+r /etc/apt/keyrings/docker.asc
# Add the repository to Apt sources:
RUN echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
    $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
    tee /etc/apt/sources.list.d/docker.list > /dev/null
RUN apt-get update

RUN apt-get install --no-install-recommends -y docker-ce docker-ce-cli containerd.io 
RUN apt-get install --no-install-recommends -y docker-buildx-plugin docker-compose-plugin 

RUN apt-get install --no-install-recommends -y systemctl
# RUN systemctl enable docker.service && systemctl enable containerd.service
# RUN mkdir -p /run/containerd && touch /run/containerd/containerd.sock
COPY init.sh /init.sh
RUN chmod +x /init.sh
ENTRYPOINT /init.sh
# ENTRYPOINT ["dockerd"]

# USER jenkins
# ENTRYPOINT [ "/usr/bin/tini", "--", "/usr/local/bin/jenkins.sh" ]
