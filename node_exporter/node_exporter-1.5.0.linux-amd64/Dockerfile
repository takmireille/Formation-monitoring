FROM bitnami/node-exporter
RUN apt install -y sudo
RUN sudo apt sudo update
RUN sudo apt upgrade
ARG ARCH="amd64"
ARG OS="linux"
LABEL maintainer="The Prometheus Authors <prometheus-developers@googlegroups.com>"

#COPY .build/${OS}-${ARCH}/node_exporter /bin/node_exporter
RUN sudo useradd -rs /bin/false node_exporter
RUN sudo apt install wget
RUN wget  https://github.com/prometheus/node_exporter/releases/download/v1.5.0/node_exporter-1.5.0.linux-amd64.tar.gz

RUN tar -xvzf node_exporter-1.5.0.linux-adm64.tar.gz

RUN mv node_exporter-1.5.0.linux-amd64/node_exporter/usr/local/bin/

RUN chown node_exporter:node_exporter /usr/local/bin/node_exporter

EXPOSE      9100
# USER node_user
ENTRYPOINT  [ "/bin/node_exporter" ]
