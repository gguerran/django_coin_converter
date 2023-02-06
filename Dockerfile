FROM python:3.10-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV APP_HOME=/home/app

RUN mkdir -p $APP_HOME

WORKDIR $APP_HOME

COPY . $APP_HOME

RUN pip install --upgrade --no-cache pip
RUN pip install --no-cache-dir -r $APP_HOME/requirements.txt

COPY ./entrypoint.sh .
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["/home/app/entrypoint.sh"]

