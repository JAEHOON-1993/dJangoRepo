FROM python:3.8

RUN mkdir /backend
WORKDIR /backend

ADD . /backend/
RUN pip install --upgrade pip && pip install -r requirements.txt
RUN python manage.py collectstatic --noinput --clear
