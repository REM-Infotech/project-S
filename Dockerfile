FROM python:3

COPY . /api
WORKDIR /api

RUN pip install Flask mysql-connector-python
CMD python main.py

