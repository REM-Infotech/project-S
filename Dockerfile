FROM python:3
COPY . /APIProexpress
RUN pip install flask && pip install pandas
WORKDIR /APIProexpress
CMD python api.py

