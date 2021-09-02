## base image
FROM python:3.9-alpine AS compile-image

## install dependencies
RUN rm -rf /var/cache/apk/* && \
    apk update && \
    apk add make && \
    apk add gcc && \
    apk add python3-dev && \
    apk add libffi-dev && \
    apk add postgresql-dev && \
    apk add gettext && \
    apk add gettext-dev && \
    apk add musl-dev && \
    apk add openssl-dev && \
    apk add build-base && \
    rm -rf /var/cache/apk/*

## virtualenv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

## add and install requirements
RUN pip install --upgrade pip
COPY ./requirements .
RUN pip install -r dev.txt

## build-image
FROM python:3.9-alpine AS runtime-image

## install dependencies
RUN apk update && \
    apk add libpq && \
    apk add curl && \
    rm -rf /var/cache/apk/*

## copy Python dependencies from build image
COPY --from=compile-image /opt/venv /opt/venv

# PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 HOME=/home/api PATH="/opt/venv/bin:$PATH"

## add user
RUN adduser -D api
USER api:api
WORKDIR $HOME
COPY --chown=api:api . $HOME
COPY --chown=api:api ./.docker/dev/entrypoint.sh /entrypoint.sh
COPY --chown=api:api ./.docker/dev/start.sh /start.sh

EXPOSE 5000

ENTRYPOINT [ "/entrypoint.sh" ]

