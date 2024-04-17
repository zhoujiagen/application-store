FROM flink:1.19.0-scala_2.12-java17

RUN apt-get update -y && \
  apt-get install -y python3 python3-pip python3-dev && rm -rf /var/lib/apt/lists/*
RUN ln -s /usr/bin/python3 /usr/bin/python

COPY clients/python/requirements.txt /
RUN pip3 install -r /requirements.txt
