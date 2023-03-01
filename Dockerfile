FROM python:3
COPY . /app/api.py
RUN pip install Flask mysql-connector-python
WORKDIR /app 
CMD python api.py

