FROM python:3
RUN pip install flask && pip install pandas
CMD python api.py

