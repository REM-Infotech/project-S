FROM python:3
<<<<<<< HEAD
COPY . /ApiConfig
=======
COPY . /app/api.py
>>>>>>> ef722f700b4ae2a6035ceaa788ad36d7b056ab79
RUN pip install Flask mysql-connector-python
WORKDIR /ApiConfig
CMD python api.py

