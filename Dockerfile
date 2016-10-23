FROM python:3.5
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD python isserviceup/app.py
