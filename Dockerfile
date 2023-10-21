FROM python:3.10.9-bullseye

ARG APP_USER=backend_user
ARG APP_GROUP=backend_group
ARG APP_USER_UID=1000
ARG VERSION=0.0.1

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install pydantic-settings
RUN pip install -r requirements.txt

ENV PYTHONPATH=/app PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

RUN groupadd --gid ${APP_USER_UID} --system ${APP_GROUP}
RUN useradd --uid ${APP_USER_UID} \
            --gid ${APP_GROUP} \
            --no-create-home \
            --system \
            --shell /bin/false \
            ${APP_USER}


COPY . .

RUN chown -R ${APP_USER}:${APP_GROUP} .

RUN echo "VERSION = '${VERSION}'" > /app/app/version.py

LABEL version="${VERSION}"

USER ${APP_USER}
