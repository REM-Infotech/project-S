FROM python:3
RUN pip install Flask mysql-connector-python 
CMD python api.py

