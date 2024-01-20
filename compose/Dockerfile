FROM python:3.11-slim

COPY monkey /opt/monkey

# User and rights
RUN useradd app -u 1000 -g 100
RUN chown -R app /opt/monkey
USER app

# Start in this directory
WORKDIR /opt/monkey