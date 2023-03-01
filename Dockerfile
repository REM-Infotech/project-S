FROM python:3
COPY . /api/main.py
RUN pip install Flask mysql-connector-python
CMD python /api/main.py

