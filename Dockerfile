FROM python:3
COPY . /app
RUN pip install Flask mysql-connector-python
WORKDIR /app 
CMD python api.py

