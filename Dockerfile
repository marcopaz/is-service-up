FROM python:3.5

ENV INSTALL_PATH /isserviceup
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -c "isserviceup/config/gunicorn.py" isserviceup.app:app
