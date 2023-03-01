FROM python:3
COPY . main.py
COPY . mysql_config.py
RUN pip install Flask mysql-connector-python
CMD python main.py

