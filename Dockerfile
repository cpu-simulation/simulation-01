### For Linux based on Debian ###

# FROM python:3.10-slim-bullseye

# RUN apt-get update\
#   && apt-get install -y --no-install-recommends --no-install-suggests \
#   python3-dev build-essential \
#   && pip install --no-cache-dir --upgrade pip


### For Linux based on Arch ###
FROM hub.hamdocker.ir/library/archlinux:base

RUN pacman -Syu --noconfirm 
RUN pacman -S --noconfirm python python-pip base-devel
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir --upgrade pip setuptools

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --requirement /app/requirements.txt

COPY . .

EXPOSE 8000 
CMD ["python3", "app.py"]
