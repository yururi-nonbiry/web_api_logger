FROM python:3.8.9-slim as django
USER root

RUN apt-get update && apt-get install -y \
    locales \
    build-essential \
    python \
    python3-dev \
    default-libmysqlclient-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
    
RUN localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

# pip関連インストール
RUN mkdir /app && mkdir /project
COPY docker/pip_install_list.txt /app
RUN pip install --upgrade pip && \
    pip install --upgrade setuptools && \
    pip install -r /app/pip_install_list.txt

# djangoファイルコピー
COPY docker/project/ /project/

#コマンド関係
WORKDIR /project
RUN python3 manage.py makemigrations
RUN python3 manage.py makemigrations project

