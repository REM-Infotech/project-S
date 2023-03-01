FROM python:3
COPY . api.py
RUN pip install Flask mysql-connector-python
CMD python api.py

