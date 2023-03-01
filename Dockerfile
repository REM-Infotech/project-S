FROM python:3
COPY . /ApiConfig
RUN pip install Flask mysql-connector-python
WORKDIR /ApiConfig
CMD python api.py

