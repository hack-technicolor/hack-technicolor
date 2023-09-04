FROM debian:bullseye-slim

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /hack-technicolor-docs

RUN apt-get update && \
    apt-get -y install python3 python3-pip git && \
    rm -rf /var/lib/apt/lists/* && \
    pip3 install mkdocs mkdocs-material mkdocs-pdf-export-plugin && \
    git clone https://github.com/hack-technicolor/hack-technicolor.git .

EXPOSE 8000

ENTRYPOINT ["mkdocs"]
CMD ["serve", "--dev-addr", "0.0.0.0:8000", "--config-file", "mkdocs.yml"]



