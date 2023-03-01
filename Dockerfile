FROM python:3

WORKDIR /api
COPY main.py /api
RUN pip install Flask mysql-connector-python
CMD python main.py

