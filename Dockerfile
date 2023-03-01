FROM python:3
COPY . main.py
RUN pip install Flask mysql-connector-python
CMD python main.py

